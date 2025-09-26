import pyautogui
import time

time.sleep(5)
print(pyautogui.size())
pyautogui.moveTo(100, 100, 3)
print(pyautogui.position())
pyautogui.moveRel(200, 200, 3)
pyautogui.click(200, 200, 2, 3, button='right')

# pyautogui.doubleClick()
# pyautogui.tripleClick()
# pyautogui.scroll(200) # Scroll up
# pyautogui.scroll(-200) # Scroll down
# pyautogui.typewrite("Hello, World!", 0.1)
# pyautogui.press("enter")
# pyautogui.leftClick()
# pyautogui.rightClick()
# pyautogui.mouseDown(100, 100, button='left')
# pyautogui.mouseUp(100, 100, button='left')
