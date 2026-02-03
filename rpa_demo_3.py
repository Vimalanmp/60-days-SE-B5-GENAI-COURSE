import pyautogui
import time
import webbrowser

# Step 1: Open browser
webbrowser.open("https://www.chatgpt.com")
time.sleep(5)  # wait for browser to open

# Step 2: Click on search bar (adjust x,y to your screen)
pyautogui.click(474, 316)  # Adjust as needed
time.sleep(1)

# Step 3: Type the search query
pyautogui.write("India vs Pakistan U-19 World Cup 2026", interval=0.05)
pyautogui.press("enter")
time.sleep(5)  # wait for results to load

# Step 4: Click first link (adjust x,y to the first link's location)
pyautogui.click(400, 650)  # Adjust as needed
