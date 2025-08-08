#### SecureClipboard
A little python script for linux to encrypt words in your clipboard

____
#### FEATURES
- Replaced Base64 with AES-256-CBC (industry-standard symmetric encryption)
- Uses random IVs per encryption (prevents pattern analysis)
- PKCS7 padding for block alignment
- 32-byte key (256-bit strength) - you must set your own
- Base64 only used for transport (not security)
- Works against clipboard sniffers (malicious sites/apps)
- secure against keyloggers or compromised systems

> 💡 Pro Tip: For maximum security, store the key in an environment variable instead of the script (requires minor code changes). Base64 was never encryption - this implementation uses proper cryptography while maintaining the same workflow.

> Warning: 🔒 Never share your key - it's hardcoded in the script

__________
**HOW IT WORKS:** First, you need run the app. then select text you want and then select terminal and press on 'c' button and then hover your mouse over anyplace you wish to paste the text and open termina to be in focus but same time over your mouse over the text field and press 'v' and thats it :D. in the background when you press 'c' it takes the text and converts it into base64 as sort of hiding data and when you press 'v' it truns it back to normal text so it can be pain in the ass if you copied a lot of text so be aware!

##---------##

**WHAT YOU NEED:** Install those packages: 
```
pip install pyperclip
pip install os
pip install sys
pip install base64
pip install pynput
pip install pyautogui

```
and then install `sudo apt-get install xclip xsel -y` and `sudo apt-get install python3-tk python3-dev`

And you need to be using ***python 3.7.3*** (*due python3-tk and python3-dev packages*)

##---------##

If you got any problems, feel free to ask
