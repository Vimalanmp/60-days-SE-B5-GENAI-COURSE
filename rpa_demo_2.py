import pyautogui
import time


"""
time.sleep(3)   # Time to switch to Notepad
pyautogui.write("Working")
"""
# Keyboard operations
"""""
pyautogui.click(979, 579)
time.sleep(1)
#pyautogui.write("python rpa_demo_2.py")
#pyautogui.press("Enter")
pyautogui.hotkey("ctrl", "a") 
"""

#image

location = pyautogui.locateOnScreen("image1.png")
print(location)

