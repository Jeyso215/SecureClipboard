## Python 3.7.3
#!/usr/bin/python3

import pyperclip ## To access the clipboard the copy and paste functions
import os ## To exit and clear the terminal
import sys ## To show the errors
import base64 ## To convert text as sort of "encrypt"
import pyautogui ## To Paste the text and get your current mouse place to paste it where your mouse at
from pynput import keyboard ## To record your keybaord and know when you clicked on 'c' or 'v' buttons

## The welcome message, i dont need to explain it right? lol
print("\nWelcome to my little humble app! please if you found any errors report them.")


def on_press(key):
    """Here all the work done"""
    try:
        ## See when you clicked on 'c' to copy data and same, see the 'v' to paste it
        if key.char.lower() == "c" :
            os.system('cls' if os.name == 'nt' else 'clear')
            pyperclip.copy(base64.b64encode(str(os.popen('xsel').read()).encode('utf-8')).decode('utf-8'))
            print("\nCopied, done\n\nNow Press 'v' to paste the copied data\n\n\nPlease note: to paste text, hover your mouse on the place you wish to paste text in and then select the terminal (but keep your mouse in same place) and press 'v' and wait sometime if it's long text")
        elif key.char.lower() == "v":
            pyautogui.click(pyautogui.position())
            pyautogui.typewrite(base64.b64decode(pyperclip.paste()).decode('utf-8'))
            raise SystemExit
        else:
            raise AttributeError
    except AttributeError:
        ## In case you clicked on wrong buttons
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Please press 'c' to copy (After you select the text) or 'v' to show copied text or 'ESC' if you want to leave")
    except SystemExit:
        ## Due some weird-crazy stuff happens while you deal with long texts, the app will leave after it finishes
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nDue some weird stuff happens with long texts, the app exits after it finishes") 
        sys.exit()  
    except:
        ## Print any other error to solve it
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


