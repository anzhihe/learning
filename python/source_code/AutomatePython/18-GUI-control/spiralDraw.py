import pyautogui
import time

time.sleep(5)
pyautogui.click()
distance = 200
dur = 0.01

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=dur)    # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=dur)    # move down
    pyautogui.dragRel(-distance, 0, duration=dur)   # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=dur)   # move up