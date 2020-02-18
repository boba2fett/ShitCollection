from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip

pyperclip.copy('Laal')
print(pyperclip.paste())


keyboardController = Controller()
keyboardController.press(Key.ctrl.value)
keyboardController.press('x')
keyboardController.release('x')
keyboardController.release(Key.ctrl.value)


# The key combination to check
COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl}

# The currently active modifiers
current = set()
def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            print('All modifiers active!')
    if key == keyboard.Key.esc:
        listener.stop()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()