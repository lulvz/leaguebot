import pyautogui

from clicks import *
from audiohandler import *

class LobbyHandler:
    def __init__(self, accept_file, wait_file, champ_file, lock_file):
        self.accept_file = accept_file
        self.wait_file = wait_file
        self.champ_file = champ_file
        self.lock_file = lock_file

    def accept(self):
        print("waiting for accept...")
        while 1:
            try:
                pos = pyautogui.locateOnScreen(self.accept_file, confidence=0.8)
                if(pos != None):
                    left_click_location(pos.left + int(pos.width/2), pos.top + int(pos.height/2))
                    break
            except KeyboardInterrupt:
                break

    def select_champ(self):
        try:
            print("waiting for champ select...")
            while 1:
                if(pyautogui.locateOnScreen(self.wait_file) != None):
                    pos = pyautogui.locateOnScreen(self.champ_file, confidence=0.8)
                    if(pos != None):
                        left_click_location(pos.left + int(pos.width/2), pos.top + int(pos.height/2))
                        pos = pyautogui.locateOnScreen(self.lock_file, confidence=0.8)
                        if(pos != None):
                            left_click_location(pos.left + int(pos.width/2), pos.top + int(pos.height/2))
                            break
        except KeyboardInterrupt:
            pass