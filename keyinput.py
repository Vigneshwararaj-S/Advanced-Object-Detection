import ctypes
import pynput
from pynput.keyboard import Key, Listener, KeyCode
from pynput import keyboard
import time

SendInput = ctypes.windll.user32.SendInput

keys = {
    "w":0x11,
    "a":0x1E,
    "s":0x1F,
    "d":0x20,
    "SPACE":0x39,

    # other inputs
    #"esc":0x01,
    #"1":0x02,
    #"2":0x03,
    #"3":0x04,
    #"4":0x05,
    #"5":0x06,
    #"6":0x07,
    #"7":0x08,
    #"8":0x09,
    #"9":0x0A,
    #"0":0x0B,
    #"-":0x0C,
    #"=":0x0D,
    #"backspace":0x0E,
    #"tab":0X0F,
    #"q":0x10,
    #"e":0x12,
    #"r":0x13,
    #"t":0x14,
    #"y":0x15,
    #"u":0x16,
    #"i":0x17,
    #"o":0x18,
    #"p":0x19,
    "enter":0x1C,
    "L CTRL":0x1D,
    #"f":0x21,
    #"g":0x22,
    #"h":0x23,
    #"j":0x24,
    #"k":0x25,
    #"l":0x26,
    "L shift":0x27,
    #"z":0x2C,
    #"x":0x2D,
    #"c":0x2E,
    #"v":0x2F,
    #"b":0x30,
    #"n":0x31,
    #"m":0x32


}
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


from ctypes import windll, Structure, c_long, byref

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]





def press_key(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, keys[key], 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def release_key(key):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, keys[key], 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
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



    
        


