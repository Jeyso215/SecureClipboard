# encrypted-clipbaord
A little python script for linux to encrypt words in your clipboard

##---------##

**HOW IT WORKS:** The app running in background, when you select a words and click on 'c' button the app catch the selected words and then convert it to base64 then save it into your clipboard and when you press 'v' button it gets the base64 copied data then switch it back to normal text and display it

##---------##

**WHAT YOU NEED:** Install packages: 
```
pip install pyperclip
pip install os
pip install sys
pip install base64
pip install pynput
pip install pyautogui

```
and then install `sudo apt-get install xclip xsel -y` and `sudo apt-get install python3-tk python3-dev`

And you need to be using ***python 3.7.3*** (*due python3-tk python3-dev packages*)

##---------##

If you got any problems, feel free to ask