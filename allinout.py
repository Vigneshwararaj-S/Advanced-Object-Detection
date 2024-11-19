#Code to move the mouse and other stuff..

#Code for direct input
import ctypes
import time
import pynput
from pynput.keyboard import Key, Listener, KeyCode
from pynput import keyboard

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

# Actuals Functions

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

def MouseMoveTo(x, y):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.mi = MouseInput(x, y, 0, 0x0001, 0, ctypes.pointer(extra))

    command = Input(ctypes.c_ulong(0), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))

def set_pos(x, y):
    x = 1 + int(x * 65536./1920.)
    y = 1 + int(y * 65536./1080.)
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(x, y, 0, (0x0001 | 0x8000), 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    command=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(command), ctypes.sizeof(command))
    
def left_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0004, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def hold_left_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0002, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_left_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0004, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def right_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
    
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0010, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def hold_right_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0008, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def release_right_click():
    extra = ctypes.c_ulong(0)
    ii_ = pynput._util.win32.INPUT_union()
    ii_.mi = pynput._util.win32.MOUSEINPUT(0, 0, 0, 0x0010, 0, ctypes.cast(ctypes.pointer(extra), ctypes.c_void_p))
    x=pynput._util.win32.INPUT(ctypes.c_ulong(0), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    #PressKey(0x11)
    #MouseMoveTo(25, 100)
    #time.sleep(1)
    #ReleaseKey(0x11)
    x =0
    y =0
    #for i in range (10):
        #MouseMoveTo(x,y+10)
        #time.sleep(0.25)
    set_pos(x+150, y+100)
    left_click()
