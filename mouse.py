#! python3
# mouse.py - Displays the mouse cursor's current position.

import pyautogui, sys

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        display = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        display += ' RGB: (' + str(pixelColor[0]).rjust(3)
        display += ', ' + str(pixelColor[1]).rjust(3)
        display += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(display, end='')
        print('\b' * len(display), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')
