from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys


if len(sys.argv)<2:
    print('Usage: insfiles.py fileToRead')
    sys.exit(1)

filename=sys.argv[1]
f=open(filename,"r")

usekey=''
print('Define the Key to use:')

def on_press(key):
    global usekey
    if key == Key.esc:
        f.close()
        return False  # stop listener
    if usekey=='':
        usekey=key
        print('Will use: '+str(usekey))
    elif key==usekey:
        print('UseKey pressed: ' + str(key))
        line = f.readline()
        if not line:
            print('------Reached End of File-----------')
            f.close()
            return False
        else:
            pyperclip.copy(line.strip())
            print(pyperclip.paste())
            
            try:
                keyboardController = Controller()
                keyboardController.press(Key.ctrl.value)
                keyboardController.press('v')
                keyboardController.release('v')
                keyboardController.release(Key.ctrl.value)
            except:
                print('failed to press crtl-v')


listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
