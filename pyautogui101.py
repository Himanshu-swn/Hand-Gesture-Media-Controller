import time
import pyautogui

time.sleep(4)  # will make the program wait for 4 sec

pyautogui.hotkey('ctrl', 'shift', '`')      # to press combinatin of keys
time.sleep(1)
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)
for i in range(10):
    # pyautogui.click(x=787, y=73)          # click at (787,73) on screen
    pyautogui.write('hehe Gotcha !!!')      # to type anything
    pyautogui.press('enter')                # to press a key 

# print(pyautogui.position())    # to get current position of mouse