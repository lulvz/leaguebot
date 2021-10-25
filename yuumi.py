from win32api import SetCursorPos
from clicks import *
from audiohandler import *
from math import sqrt
from time import sleep

class YuumiBot:
    def __init__(self, spells=["heal", "barrier"], intensity = 250):
        self.spells = spells
        self.command_list = {
            "bomb" : 1,
            "missile" : 1,
            "potato" : 1,
            "go in" : 2,
            "going" : 2,
            "enter" : 2,
            "come" : 2,
            "pineapple" : 2,
            "banana" : 3,
            "heal" : 3,
            "ultimate" : 4,
            "ult" : 4,
            "melon" : 4,
            "direction" : 5,
            "mango" : 5,
            "increase" : 6,
            "decrease" : 7,
            "degrees" : 7,
            "stop" : 8
        }
        # the amount of pixels that the mouse should move in each direction
        self.intensity = intensity
        # the default directions
        self.directions = {
            "up" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) - self.intensity),
            "right" : (int(win32api.GetSystemMetrics(0)/2) + self.intensity, int(win32api.GetSystemMetrics(1)/2)),
            "down" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) + self.intensity),
            "left" : (int(win32api.GetSystemMetrics(0)/2) - self.intensity, int(win32api.GetSystemMetrics(1)/2)),

            "upright" : (int(win32api.GetSystemMetrics(0)/2 + self.intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - self.intensity*sqrt(2)/2)),
            "downright" : (int(win32api.GetSystemMetrics(0)/2 + self.intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + self.intensity*sqrt(2)/2)),
            "downleft" : (int(win32api.GetSystemMetrics(0)/2 - self.intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + self.intensity*sqrt(2)/2)),
            "upleft" : (int(win32api.GetSystemMetrics(0)/2 - self.intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - self.intensity*sqrt(2)/2))
        }
        # the stored current direction
        self.current_direction = (0,0)
        # AudioHandler created
        self.ah = AudioHandler()

    # set the direction
    def set_direction(self, direction):
        self.current_direction = self.directions[direction]

    def set_intensity(self, intensity):
        self.directions = {
            "up" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) - intensity),
            "right" : (int(win32api.GetSystemMetrics(0)/2) + intensity, int(win32api.GetSystemMetrics(1)/2)),
            "down" : (int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2) + intensity),
            "left" : (int(win32api.GetSystemMetrics(0)/2) - intensity, int(win32api.GetSystemMetrics(1)/2)),

            "upright" : (int(win32api.GetSystemMetrics(0)/2 + intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - intensity*sqrt(2)/2)),
            "downright" : (int(win32api.GetSystemMetrics(0)/2 + intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + intensity*sqrt(2)/2)),
            "downleft" : (int(win32api.GetSystemMetrics(0)/2 - intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 + intensity*sqrt(2)/2)),
            "upleft" : (int(win32api.GetSystemMetrics(0)/2 - intensity*sqrt(2)/2), int(win32api.GetSystemMetrics(1)/2 - intensity*sqrt(2)/2))
        }

    def stop(self):
        keyboard_click(DIK_S)

    def q(self, direction):
        SetCursorPos(direction)
        keyboard_click(DIK_Q)

    def w(self, person):
        if (person == 1):
            PressKey(DIK_Z)
            center_cursor()
            sleep(0.5)
            keyboard_click(DIK_W)
            ReleaseKey(DIK_Z)
        elif (person == 2):
            PressKey(DIK_X)
            center_cursor()
            sleep(0.5)
            keyboard_click(DIK_W)
            ReleaseKey(DIK_X)
        elif (person == 3):
            PressKey(DIK_C)
            center_cursor()
            sleep(0.5)
            keyboard_click(DIK_W)
            ReleaseKey(DIK_C)
        elif (person == 4):
            PressKey(DIK_V)
            center_cursor()
            sleep(0.5)
            keyboard_click(DIK_W)
            ReleaseKey(DIK_V)
        elif (person == 0): 
            keyboard_click(DIK_W)
        
    def e(self):
        keyboard_click(DIK_E)

    def r(self, direction):
        SetCursorPos(direction)
        keyboard_click(DIK_R)

    def spell(self, spell):
        if (spell == 1):
            keyboard_click("d")
        elif (spell == 2):
            keyboard_click("f")

    def play(self):
        while 1:
            try:
                print("waiting for speech")
                speech = self.ah.process_speech().lower()
                print(speech)
                for keyword in self.command_list.keys():
                    if (keyword in speech):
                        
                        # Yuumi Q
                        if self.command_list[keyword] == 1:
                            self.q(self.current_direction)

                        # Yuumi W
                        elif self.command_list[keyword] == 2:
                            if ("1" in speech or "one" in speech or "on" in speech):
                                self.w(1)
                            elif ("2" in speech or "two" in speech or "to" in speech):
                                self.w(2)
                            elif ("3" in speech or "three" in speech or "tree" in speech):
                                self.w(3)
                            elif ("4" in speech or "four" in speech or "for" in speech):
                                self.w(4)
                        
                        # Yuumi E
                        elif self.command_list[keyword] == 3:
                            self.e()

                        # Yuumi R
                        elif self.command_list[keyword] == 4:
                            self.r(self.current_direction)

                        # Set direction to use ult and q
                        elif self.command_list[keyword] == 5:
                            if ("1" in speech or "one" in speech):
                                print("setting direction 1")
                                self.set_direction("up")
                            elif ("2" in speech or "two" in speech or "to" in speech):
                                self.set_direction("upright")
                                print("setting direction 2")
                            elif ("3" in speech or "three" in speech or "tree" in speech):
                                self.set_direction("right")
                                print("setting direction 3")
                            elif ("4" in speech or "four" in speech or "for" in speech):
                                self.set_direction("downright")
                                print("setting direction 4")
                            elif ("5" in speech or "five" in speech or "fire" in speech):
                                self.set_direction("down")
                                print("setting direction 5")
                            elif ("6" in speech or "six" in speech or "ziggs" in speech):
                                self.set_direction("downleft")
                                print("setting direction 6")
                            elif ("7" in speech or "sven" in speech or "seven" in speech):
                                self.set_direction("left")
                                print("setting direction 7")
                            elif ("8" in speech or "ate" in speech or "eight" in speech):
                                self.set_direction("upleft")
                                print("setting direction 8")
                        
                        # Set intensity to use ult and q
                        elif self.command_list[keyword] == 6:
                            print("increase itensity by 50")
                            self.intensity += 50
                            self.set_intensity((self.intensity+50))
                            print("current intensity = " + str(self.intensity))
                        elif self.command_list[keyword] == 7:
                            print("decrease itensity by 50")
                            self.intensity -= 50
                            self.set_intensity((self.intensity-50))
                            print("current intensity = " + str(self.intensity))
                            
                        elif self.command_list[keyword] == 8:
                            self.stop()

            except Exception as e:
                if (Exception == KeyboardInterrupt):
                    break
                else:
                    print(e)