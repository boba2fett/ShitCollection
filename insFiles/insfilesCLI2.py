from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys


f=''
usekey=''


def on_press(key):
    global usekey
    if key == Key.esc:
        f.close()
        return False  # stop listener
    if usekey=='':
        usekey=key
        #print('Will use: '+str(usekey))
    elif key==usekey:
        #print('UseKey pressed: ' + str(key))
        line = f.readline()
        if not line:
            #print('Reached EOF')
            f.close()
            return False
        else:
            pyperclip.copy(line.strip())
            #print(pyperclip.paste())
            
            try:
                keyboardController = Controller()
                keyboardController.press(Key.ctrl.value)
                keyboardController.press('v')
                keyboardController.release('v')
                keyboardController.release(Key.ctrl.value)
            except:
                #print('failed to press crtl-v')


def main(filename):
    "Insert line by line of a file into a GUI by just pressing a key"
    global f
    f=open(filename,"r")
    #print('Define the Key to use by pressing it:')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


if __name__ == '__main__':
    import plac; plac.call(main)

