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

# 🔑 CRITICAL: SET YOUR OWN 32-BYTE KEY BELOW (MUST BE EXACTLY 32 CHARACTERS)
# Generate securely with: openssl rand -base64 32 | tr -d '\n=' | cut -c-32
KEY = b'Your32ByteAES256EncryptionKey!!'  # CHANGE THIS IMMEDIATELY

print("\nWelcome to SecureClipboard! Using AES-256 encryption. Press 'c' to copy or 'v' to paste.")

def on_press(key):
    try:
        if key.char.lower() == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            selected_text = os.popen('xsel').read().encode('utf-8')

            # AES-256 encryption with random IV
            iv = get_random_bytes(16)
            cipher = AES.new(KEY, AES.MODE_CBC, iv)
            ciphertext = cipher.encrypt(pad(selected_text, AES.block_size))

            # Base64 only for clipboard transport (not security)
            encrypted_data = base64.b64encode(iv + ciphertext).decode('utf-8')
            pyperclip.copy(encrypted_data)

            print("\n✅ Encrypted to clipboard (AES-256). Press 'v' to paste.")

        elif key.char.lower() == "v":
            encrypted_data = pyperclip.paste()
            try:
                # Decode and split IV/ciphertext
                data = base64.b64decode(encrypted_data)
                iv, ciphertext = data[:16], data[16:]

                # Decrypt
                cipher = AES.new(KEY, AES.MODE_CBC, iv)
                decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')

                # Paste at cursor
                pyautogui.click(pyautogui.position())
                pyautogui.typewrite(decrypted)
                raise SystemExit

            except (ValueError, KeyError) as e:
                print(f"\n❌ Decryption failed: {str(e)}\nEnsure you're pasting data encrypted with THIS tool.")

        else:
            raise AttributeError

    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Press 'c' to copy, 'v' to paste, or 'ESC' to quit")
    except SystemExit:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nOperation completed. Exiting for security.")
        sys.exit()
    except Exception as e:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n🚨 Critical error: {type(e).__name__}\nReport this to developer.")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
