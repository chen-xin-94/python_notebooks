import time
import pyautogui

# move to the center of the monitor and click once every minute
while True:
    pyautogui.click(pyautogui.size().width/2,pyautogui.size().height/2)
    time.sleep(600)

