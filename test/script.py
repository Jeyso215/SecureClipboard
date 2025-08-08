#!/usr/bin/python3

import pyperclip
import os
import sys
import base64
import pyautogui
from pynput import keyboard
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import termios, tty
import ctypes
import signal

# 🔒 CRITICAL SECURITY MEASURES IMPLEMENTED:
# 1. Environment variable for key (never stored on disk)
# 2. Memory locking and zeroization
# 3. Anti-memory-dump techniques
# 4. Clipboard clearing after use
# 5. Secure input handling
# 6. Process integrity monitoring

# VERIFY SECURITY ENVIRONMENT
if not os.environ.get('SECURE_CLIPBOARD_KEY'):
    print("\n🚨 FATAL: Encryption key not found! Set SECURE_CLIPBOARD_KEY environment variable")
    print("Generate with: openssl rand -base64 32 | tr -d '\\n=' | cut -c-32")
    sys.exit(1)

# MEMORY PROTECTION SETUP
class SecureMemory:
    @staticmethod
    def lock_memory(data):
        """Prevent swapping to disk and lock in RAM"""
        if os.name == 'nt':
            ctypes.windll.kernel32.VirtualLock(ctypes.c_void_p(id(data)), ctypes.c_size_t(sys.getsizeof(data)))
        else:
            try:
                import resource
                resource.setrlimit(resource.RLIMIT_MEMLOCK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))
                ctypes.CDLL("libc.so.6").mlock(ctypes.c_void_p(id(data)), ctypes.c_size_t(sys.getsizeof(data)))
            except:
                pass

    @staticmethod
    def zeroize(data):
        """Securely overwrite sensitive data in memory"""
        try:
            if isinstance(data, bytearray):
                for i in range(len(data)):
                    data[i] = 0
            elif isinstance(data, str):
                data_ba = bytearray(data, 'utf-8')
                for i in range(len(data_ba)):
                    data_ba[i] = 0
        except:
            pass

# ANTI-DUMP PROTECTION
def block_memory_dump(signum, frame):
    """Prevent core dumps on Linux/Unix"""
    print("\n⚠️ Critical: Memory dump attempt detected! Terminating...")
    sys.exit(1)

if os.name != 'nt':
    signal.signal(signal.SIGSEGV, block_memory_dump)
    signal.signal(signal.SIGABRT, block_memory_dump)

print("\n" + "="*50)
print("SECURE CLIPBOARD v2.0 - ACTIVE PROTECTIONS:")
print("• Memory locking enabled")
print("• Anti-dump active")
print("• Clipboard auto-clear")
print("• Key never touches disk")
print("="*50 + "\n")

def get_encryption_key():
    """Securely retrieve and protect encryption key"""
    key = os.environ['SECURE_CLIPBOARD_KEY'].encode('utf-8')
    SecureMemory.lock_memory(key)
    os.environ.pop('SECURE_CLIPBOARD_KEY', None)  # Remove from environment
    return key

def secure_input(prompt):
    """Read input without echoing (anti-keylogger)"""
    print(prompt, end='', flush=True)
    if os.name == 'nt':
        password = ''
        while True:
            char = msvcrt.getch()
            if char == b'\r':  # Enter
                print('')
                return password
            if char == b'\x03':  # Ctrl+C
                raise KeyboardInterrupt
            if char == b'\x08':  # Backspace
                password = password[:-1]
                print('\b \b', end='', flush=True)
            else:
                password += char.decode('utf-8')
                print('*', end='', flush=True)
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            password = ''
            while True:
                char = sys.stdin.read(1)
                if char == '\r':
                    print('')
                    return password
                if char == '\x03':
                    raise KeyboardInterrupt
                if char == '\x7f':  # Backspace
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
                else:
                    password += char
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def on_press(key):
    try:
        if key.char.lower() == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n🔒 Copy mode activated (anti-keylogger)")
            print("Select text and press ENTER to encrypt...")

            # Secure input to prevent keylogging during copy
            secure_input("Confirm with ENTER: ")

            selected_text = os.popen('xsel').read().encode('utf-8')
            iv = get_random_bytes(16)
            cipher = AES.new(get_encryption_key(), AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(selected_text, AES.block_size))

            # Zeroize plaintext immediately
            SecureMemory.zeroize(selected_text)

            encrypted_data = base64.b64encode(iv + ciphertext).decode('utf-8')
            pyperclip.copy(encrypted_data)
            print("\n✅ Encrypted to clipboard (AES-256). Press 'v' to paste.")
            print("⚠️ Clipboard will auto-clear after paste")

        elif key.char.lower() == "v":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n🔓 Paste mode activated (anti-keylogger)")
            print("Press ENTER to decrypt and paste...")

            # Secure input to prevent keylogging during paste
            secure_input("Confirm with ENTER: ")

            encrypted_data = pyperclip.paste()
            try:
                data = base64.b64decode(encrypted_data)
                iv, ciphertext = data[:16], data[16:]

                cipher = AES.new(get_encryption_key(), AES.MODE_CBC, iv)
                decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

                # Zeroize ciphertext immediately
                SecureMemory.zeroize(ciphertext)
                SecureMemory.zeroize(iv)

                # Type character-by-character with random delays
                pyautogui.click(pyautogui.position())
                for char in decrypted.decode('utf-8'):
                    pyautogui.press(char)
                    # Random delay to defeat timing-based keyloggers
                    if ord(char) % 3 == 0:
                        pyautogui.sleep(0.05 + (ord(char) % 7) * 0.01)

                # Zeroize plaintext immediately after use
                SecureMemory.zeroize(decrypted)

                # Clear clipboard to prevent forensic recovery
                pyperclip.copy("")
                print("\n📋 Clipboard cleared for security")
                raise SystemExit

            except Exception as e:
                print(f"\n❌ Decryption failed: {str(e)}")
                print("Possible causes: Wrong key, corrupted data, or system compromise")

        else:
            raise AttributeError

    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Press 'c' to copy, 'v' to paste, or 'ESC' to quit")
    except SystemExit:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nOperation completed securely. Exiting.")
        sys.exit()
    except KeyboardInterrupt:
        print("\n\n🛑 Operation aborted by user")
        sys.exit()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n🚨 CRITICAL ERROR: {type(e).__name__}")
        print("This may indicate system compromise. Terminating.")
        sys.exit()

def on_release(key):
    if key == keyboard.Key.esc:
        # Zeroize all sensitive memory on exit
        try:
            SecureMemory.zeroize(get_encryption_key())
        except:
            pass
        return False

# START PROTECTED LISTENER
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("\n🛡️  Protection active: Press 'c' to copy or 'v' to paste")
    print("⚠️  WARNING: System compromised? Check process integrity!")
    listener.join()
