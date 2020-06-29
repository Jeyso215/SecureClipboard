# encrypted-clipbaord
A little python script for linux to encrypt words in your clipboard
<br>
**HOW IT WORKS:** The app running in background, when you select a words and click on 'c' button the app catch the selected words and then convert it to base64 then save it into your clipboard and when you press 'v' button it gets the base64 copied data then switch it back to normal text and display it
<br>
**WHAT YOU NEED:** Install packages: 
```
pip install clipboard
pip install os
pip install sys
pip install base64
pip install pynput
```
and then install `sudo apt-get install xclip xsel -y`
