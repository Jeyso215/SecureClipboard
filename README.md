# encrypted-clipbaord
A little python script for linux to encrypt words in your clipboard

##---------##

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