from time import sleep
from math import sqrt

from pyautogui import leftClick
from clicks import *

import pyautogui

print("clicking ....")
while 1:
    print("clicking ....")

    try:
        pos = pyautogui.locateOnScreen("./IMAGES/DOWNLOAD.PNG", confidence=0.8)
        if(pos != None):
            left_click_location(pos.left + int(pos.width/2), pos.top + int(pos.height/2))
            win32api.SetCursorPos((0,0))
    except KeyboardInterrupt:
        break

#intensity = 250
#
#directions = {
#    "up" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) - intensity),
#    "right" : (int(win32api.GetSystemMetrics(0)/2) + intensity, int(win32api.GetSystemMetrics(1)/2)),
#    "down" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) + intensity),
#    "left" : (int(win32api.GetSystemMetrics(0)/2) - intensity, int(win32api.GetSystemMetrics(1)/2)),
#
#    "upright" : (int(win32api.GetSystemMetrics(0)/2 + intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - intensity*sqrt(2)/2)),
#    "downright" : (int(win32api.GetSystemMetrics(0)/2 + intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + intensity*sqrt(2)/2)),
#    "downleft" : (int(win32api.GetSystemMetrics(0)/2 - intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + intensity*sqrt(2)/2)),
#    "upleft" : (int(win32api.GetSystemMetrics(0)/2 - intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - intensity*sqrt(2)/2))
#}
#
#print(directions)
#
#speech = "alo alo ee hehe"
#
##if "alo" or "ee" in speech:
##    print("test")
#sleep(1)
#for direction in directions:
#   win32api.SetCursorPos(directions[direction])
#   left_click()
#   sleep(0.5)

#PressKey(DIK_SPACE)
#
#right_click(900,900)
#
#sleep(1)
#
#keyboard_click(DIK_Q)
#sleep(2)
#keyboard_click(DIK_W)
#keyboard_click(DIK_E)
#keyboard_click(DIK_R) 
#
#ReleaseKey(DIK_SPACE)


#win32api.SetCursorPos((int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) - intensity))
#sleep(1)
#win32api.SetCursorPos((int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2)))