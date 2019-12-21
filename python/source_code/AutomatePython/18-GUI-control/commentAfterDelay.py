import pyautogui
import time
def commentAfterDelay():
	pyautogui.click(100, 100)
	pyautogui.typewrite('In IDLE, Alt-3 commets out a line.')
	time.sleep(2)
	pyautogui.hotkey('alt', '3')

	
commentAfterDelay()