# Import the relevant modules
import pyautogui
import time

# FAIL-SAFE - DO NOT DISABLE THIS
pyautogui.FAILSAFE = True

# Example
time.sleep(3)
text = open("message.txt")
for each_line in text:
    pyautogui.write(each_line)
