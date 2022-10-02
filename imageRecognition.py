import pyautogui, cv2

pyautogui.screenshot('/Users/julia/Documents/example_screenshot1.png')

print(pyautogui.locateOnScreen('/Users/julia/Documents/7.png'))

print(pyautogui.locateCenterOnScreen('/Users/julia/Documents/7.png'))

# print(pyautogui.position())

pyautogui.moveTo((27, 175), duration=1)
pyautogui.click()
