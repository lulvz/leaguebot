### this isnt my code ###

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actual Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


### this is my code ###
import win32api
import win32con

import time

#Giant dictonary to hold key name and VK value
VK_CODE = {'backspace':0x08,
           'tab':0x09,
           'clear':0x0C,
           'enter':0x0D,
           'shift':0x10,
           'ctrl':0x11,
           'alt':0x12,
           'pause':0x13,
           'caps_lock':0x14,
           'esc':0x1B,
           'spacebar':0x20,
           'page_up':0x21,
           'page_down':0x22,
           'end':0x23,
           'home':0x24,
           'left_arrow':0x25,
           'up_arrow':0x26,
           'right_arrow':0x27,
           'down_arrow':0x28,
           'select':0x29,
           'print':0x2A,
           'execute':0x2B,
           'print_screen':0x2C,
           'ins':0x2D,
           'del':0x2E,
           'help':0x2F,
           '0':0x30,
           '1':0x31,
           '2':0x32,
           '3':0x33,
           '4':0x34,
           '5':0x35,
           '6':0x36,
           '7':0x37,
           '8':0x38,
           '9':0x39,
           'a':0x41,
           'b':0x42,
           'c':0x43,
           'd':0x44,
           'e':0x45,
           'f':0x46,
           'g':0x47,
           'h':0x48,
           'i':0x49,
           'j':0x4A,
           'k':0x4B,
           'l':0x4C,
           'm':0x4D,
           'n':0x4E,
           'o':0x4F,
           'p':0x50,
           'q':0x51,
           'r':0x52,
           's':0x53,
           't':0x54,
           'u':0x55,
           'v':0x56,
           'w':0x57,
           'x':0x58,
           'y':0x59,
           'z':0x5A,
           'numpad_0':0x60,
           'numpad_1':0x61,
           'numpad_2':0x62,
           'numpad_3':0x63,
           'numpad_4':0x64,
           'numpad_5':0x65,
           'numpad_6':0x66,
           'numpad_7':0x67,
           'numpad_8':0x68,
           'numpad_9':0x69,
           'multiply_key':0x6A,
           'add_key':0x6B,
           'separator_key':0x6C,
           'subtract_key':0x6D,
           'decimal_key':0x6E,
           'divide_key':0x6F,
           'F1':0x70,
           'F2':0x71,
           'F3':0x72,
           'F4':0x73,
           'F5':0x74,
           'F6':0x75,
           'F7':0x76,
           'F8':0x77,
           'F9':0x78,
           'F10':0x79,
           'F11':0x7A,
           'F12':0x7B,
           'F13':0x7C,
           'F14':0x7D,
           'F15':0x7E,
           'F16':0x7F,
           'F17':0x80,
           'F18':0x81,
           'F19':0x82,
           'F20':0x83,
           'F21':0x84,
           'F22':0x85,
           'F23':0x86,
           'F24':0x87,
           'num_lock':0x90,
           'scroll_lock':0x91,
           'left_shift':0xA0,
           'right_shift ':0xA1,
           'left_control':0xA2,
           'right_control':0xA3,
           'left_menu':0xA4,
           'right_menu':0xA5,
           'browser_back':0xA6,
           'browser_forward':0xA7,
           'browser_refresh':0xA8,
           'browser_stop':0xA9,
           'browser_search':0xAA,
           'browser_favorites':0xAB,
           'browser_start_and_home':0xAC,
           'volume_mute':0xAD,
           'volume_Down':0xAE,
           'volume_up':0xAF,
           'next_track':0xB0,
           'previous_track':0xB1,
           'stop_media':0xB2,
           'play/pause_media':0xB3,
           'start_mail':0xB4,
           'select_media':0xB5,
           'start_application_1':0xB6,
           'start_application_2':0xB7,
           'attn_key':0xF6,
           'crsel_key':0xF7,
           'exsel_key':0xF8,
           'play_key':0xFA,
           'zoom_key':0xFB,
           'clear_key':0xFE,
           '+':0xBB,
           ',':0xBC,
           '-':0xBD,
           '.':0xBE,
           '/':0xBF,
           '`':0xC0,
           ';':0xBA,
           '[':0xDB,
           '\\':0xDC,
           ']':0xDD,
           "'":0xDE,
           '`':0xC0
            }

#Couldnt find a dictionary only this that creates a bunch of variables with the hex codes
#for the directx scancodes
DIK_ESCAPE=0x01
DIK_1=0x02
DIK_2               =0x03
DIK_3               =0x04
DIK_4               =0x05
DIK_5               =0x06
DIK_6               =0x07
DIK_7               =0x08
DIK_8               =0x09
DIK_9               =0x0A
DIK_0               =0x0B
DIK_MINUS           =0x0C    #/* - on main keyboard */
DIK_EQUALS          =0x0D
DIK_BACK            =0x0E    #/* backspace */
DIK_TAB             =0x0F
DIK_Q               =0x10
DIK_W               =0x11
DIK_E               =0x12
DIK_R               =0x13
DIK_T               =0x14
DIK_Y               =0x15
DIK_U               =0x16
DIK_I               =0x17
DIK_O               =0x18
DIK_P               =0x19
DIK_LBRACKET        =0x1A
DIK_RBRACKET        =0x1B
DIK_RETURN          =0x1C    #/* Enter on main keyboard */
DIK_LCONTROL        =0x1D
DIK_A               =0x1E
DIK_S               =0x1F
DIK_D               =0x20
DIK_F               =0x21
DIK_G               =0x22
DIK_H               =0x23
DIK_J               =0x24
DIK_K               =0x25
DIK_L               =0x26
DIK_SEMICOLON       =0x27
DIK_APOSTROPHE      =0x28
DIK_GRAVE           =0x29    #/* accent grave */
DIK_LSHIFT          =0x2A
DIK_BACKSLASH       =0x2B
DIK_Z               =0x2C
DIK_X               =0x2D
DIK_C               =0x2E
DIK_V               =0x2F
DIK_B               =0x30
DIK_N               =0x31
DIK_M               =0x32
DIK_COMMA           =0x33
DIK_PERIOD          =0x34    #/* . on main keyboard */
DIK_SLASH           =0x35    #/* / on main keyboard */
DIK_RSHIFT          =0x36
DIK_MULTIPLY        =0x37    #/* * on numeric keypad */
DIK_LMENU           =0x38    #/* left Alt */
DIK_SPACE           =0x39
DIK_CAPITAL         =0x3A
DIK_F1              =0x3B
DIK_F2              =0x3C
DIK_F3              =0x3D
DIK_F4              =0x3E
DIK_F5              =0x3F
DIK_F6              =0x40
DIK_F7              =0x41
DIK_F8              =0x42
DIK_F9              =0x43
DIK_F10             =0x44
DIK_NUMLOCK         =0x45
DIK_SCROLL          =0x46    #/* Scroll Lock */
DIK_NUMPAD7         =0x47
DIK_NUMPAD8         =0x48
DIK_NUMPAD9         =0x49
DIK_SUBTRACT        =0x4A    #/* - on numeric keypad */
DIK_NUMPAD4         =0x4B
DIK_NUMPAD5         =0x4C
DIK_NUMPAD6         =0x4D
DIK_ADD             =0x4E    #/* + on numeric keypad */
DIK_NUMPAD1         =0x4F
DIK_NUMPAD2         =0x50
DIK_NUMPAD3         =0x51
DIK_NUMPAD0         =0x52
DIK_DECIMAL         =0x53    #/* . on numeric keypad */
DIK_F11             =0x57
DIK_F12             =0x58
RUN_W=0x2A
RUN_S=0x2A
RUN_A=0x2A
RUN_D=0x2A

def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #PressKey(0x100)
    time.sleep(0.01)
    #ReleaseKey(0x100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    #PressKey(0x101)
    time.sleep(0.01)
    #ReleaseKey(0x101)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def left_click_location(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #PressKey(0x100)
    time.sleep(0.01)
    #ReleaseKey(0x100)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def right_click_location(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    #PressKey(0x101)
    time.sleep(0.01)
    #ReleaseKey(0x101)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def center_cursor():
    win32api.SetCursorPos((int(win32api.GetSystemMetrics(0)/2), int(win32api.GetSystemMetrics(1)/2)))

def keyboard_click(key):
    #win32api.keybd_event(VK_CODE[key], 0, 0, 0)
    PressKey(key)
    time.sleep(0.01)
    ReleaseKey(key)
    #win32api.keybd_event(VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0)
