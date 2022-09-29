import pyautogui

print(pyautogui.size())

width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())

pyautogui.moveTo(100, 100, duration=0.5)
pyautogui.moveRel(200, 0, duration=0.5)
pyautogui.moveRel(0, 100, duration=1.0)

print(pyautogui.position())

pyautogui.click(687, 14)
pyautogui.doubleClick()
pyautogui.rightClick()
