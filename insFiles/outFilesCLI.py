from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys


f=''
usekey=''
last_line=''

def on_press(key):
    global usekey
    global last_line
    if key == Key.esc:
        f.close()
        return False  # stop listener
    if usekey=='':
        usekey=key
        print('Will use: '+str(usekey))
    elif key==usekey:
        print('UseKey pressed: ' + str(key))
        
        try:
            keyboardController = Controller()
            keyboardController.press(Key.ctrl.value)
            keyboardController.press('c')
            keyboardController.release('c')
            keyboardController.release(Key.ctrl.value)
            pp=pyperclip.paste()
            if pp!=last_line:
                print(pp)
                f.write(pp+'\n')
                last_line=pp
        except:
            f.flush()
            print('failed to press crtl-c')


def main(filename):
    "Insert line by line in a file from a GUI by just pressing a key"
    global f
    f=open(filename,"w")
    print('Define the Key to use by pressing it:')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


if __name__ == '__main__':
    import plac; plac.call(main)

