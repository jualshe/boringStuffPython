# painnt online https://paint.js.org/

import pyautogui

pyautogui.click()
distance = 200
while distance > 0:
    print(distance, 0)
    pyautogui.dragRel(distance, 0, duration=1, 5)  # move right
    distance = distance - 25

    print(0, distance)
    pyautogui.dragRel()
