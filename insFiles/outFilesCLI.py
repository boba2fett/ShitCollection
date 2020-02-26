from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys


f=''
usekey=''
last_line=''
delayed=False
hook=''

def on_press(key):
    global usekey, last_line, hook, delayed
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
            if delayed:
                time.sleep(0.5)
            pp=pyperclip.paste()
            if pp!=last_line and hook in pp:
                print(pp)
                f.write(pp+'\n')
                last_line=pp
            else:
                print('Same as last')
        except:
            f.flush()
            print('failed to press crtl-c')


def main(filename,hookline: ('search for occurence of string', 'option', 's'),delay: ('make a delay before using clipboard', 'flag', 'd')):
    "Insert line by line in a file from a GUI by just pressing a key"
    global f,hook,delayed
    delayed=delay
    hook=hookline
    if not hook:
        hook=''
    f=open(filename,"w")
    print('Define the Key to use by pressing it:')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


if __name__ == '__main__':
    import plac; plac.call(main)

