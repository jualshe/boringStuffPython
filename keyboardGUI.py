import pyautogui

# pyautogui.click(200, 200);
# pyautogui.typewrite('Hello world!', interval=0.2)

pyautogui.click(200, 200);
pyautogui.typewrite(['a', 'b', 'left', 'X', 'Y'], interval=0.1)

print(pyautogui.KEYBOARD_KEYS)
pyautogui.press('del')
pyautogui.hotkey('shift', 'left', 'left', 'left')
