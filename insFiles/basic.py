import sys
from pynput.keyboard import Key, Controller
import termios
import contextlib


from pynput import keyboard


def on_press(key):
    if key == Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
        print('Key pressed: ' + k)
    except:
        try:
            k = key.name  # other keys
            print('Key pressed: ' + k)
        except:
            print('Key pressed: ' + str(key))


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
