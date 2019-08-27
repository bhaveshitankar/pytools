##############################################################################
#	author: bhavesh itankar
#	Subjet: Automated time based search result creator for Notepad++
#	Usage:  please refer readme.txt
##############################################################################


try:
	import pyautogui as agui
except SyntaxError: 
	import pyautogui as agui
import time
import keyboard
import os
############################################################################
#  enter your expected time of one search in t_ms in milli seconds
############################################################################
t_ms=100
def sercher(string):
	agui.hotkey('ctrl', 'shift', 'f')
	agui.typewrite(string)
	agui.press('enter')
agui.hotkey('alt', 'tab')
with open(os.path.dirname(os.path.abspath(__file__))+r"\word_list.txt") as FH:
	for count,line in enumerate(reversed(FH.read().split('\n')[:])):
		print(count,line)
		if not line=='':
			sercher(line)
			for i in range(t_ms): 
				time.sleep(0.01)
				if keyboard.is_pressed('ctrl'):
					break
agui.hotkey('alt', 'tab')
print('seaching is done')
