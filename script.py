## Python 3.7.3
#!/usr/bin/python3

import pyperclip
import os
import sys
import base64
import pyautogui
from pynput import keyboard


print("\nWelcome to my little humble app! please if you found any errors report them.")

def on_press(key):
    try:
        if key.char.lower() == "c" :
            os.system('cls' if os.name == 'nt' else 'clear')
            pyperclip.copy(base64.b64encode(str(os.popen('xsel').read()).encode('utf-8')).decode('utf-8'))
            print("\nCopied, done\n\nNow Press 'v' to view the copied data")
        elif key.char.lower() == "v":
            os.system('cls' if os.name == 'nt' else 'clear')
            pyautogui.click(pyautogui.position())
            pyautogui.typewrite(base64.b64decode(pyperclip.paste()).decode('utf-8'))
    except AttributeError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please press 'c' to copy (After you select the text) or 'v' to paste (After you hover your mouse in the place you want to paste the words in) or 'ESC' if you want to leave")
    except :
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nHmm, something wrong. please report the error as {sys.exc_info()[0]}")
        sys.exit()

def on_release(key):
## Get out of the app
    if key == keyboard.Key.esc:
        return False

## Start until you press the "ESC" button
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()








### ------------------------------- ###

## IN CASE I NEEDED THEM

# from Crypto.Cipher import AES
# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# message = "The answer is no"
# ciphertext = obj.encrypt(message)
# print(ciphertext)

# obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
# print(obj2.decrypt(ciphertext).decode('utf-8'))




## ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()


    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
