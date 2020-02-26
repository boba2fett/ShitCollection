from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys
import time

CRED = '\033[91m'
CEND = '\033[0m'

Fto=''
Ffrom=''
usekey=''
last_line=''
pyperclip.copy('')
hook=''
delayed=False
keyboardController = Controller()

def copyToFile():
    global Fto, Ffrom, last_line, hook, keyboardController
    try:
        #keyboardController = Controller()
        keyboardController.press(Key.ctrl.value)
        keyboardController.press('c')
        keyboardController.release('c')
        keyboardController.release(Key.ctrl.value)
        if delayed:
            print('wait')
            time.sleep(0.5)
        pp=pyperclip.paste()
        if pp!=last_line and hook in pp:
            print('Write: '+pp)
            Fto.write(pp+'\n')
            last_line=pp
            return True
        else:
            print('Same as last or '+hook+' not inside')
            return False
    except:
        print(CRED+'failed to press sth'+CEND)
        Fto.close()
        Ffrom.close()
        exit()


def pasteFromFile():
    global Fto, Ffrom
    line = Ffrom.readline()
    if not line:
        print('Reached EOF')
        Ffrom.close()
        return False
    else:
        pyperclip.copy(line.strip())
        print('Read: '+pyperclip.paste())
        
        try:
            #keyboardController = Controller()
            keyboardController.press(Key.ctrl.value)
            keyboardController.press('v')
            keyboardController.release('v')
            keyboardController.release(Key.ctrl.value)
            # auto enter
            keyboardController.press(Key.enter.value)
            keyboardController.release(Key.enter.value)
        except:
            print(CRED+'failed to press sth'+CEND)
            Fto.close()
            Ffrom.close()
            exit()
        return True


def on_press(key):
    global usekey, last_line, Ffrom, Fto
    if key == Key.esc:
        Fto.close()
        Ffrom.close()
        return False  # stop listener
    if usekey=='':# very first time
        usekey=key
        print('Will use: '+str(usekey))
    elif key==usekey:
        print('UseKey pressed: ' + str(key))
        if pyperclip.paste()=='': # first time
            pasteFromFile()
            return not Ffrom.closed
        else:
            if copyToFile():
                return pasteFromFile()


def main(readfile,writefile,hookline: ('search for occurence of string', 'option', 's'),delay: ('make a delay before using clipboard', 'flag', 'd')):
    "Insert line by line in a file from a GUI by just pressing a key (ESC exits everytime)"
    global Fto, hook, Ffrom, delayed
    Fto=open(writefile,"w")
    Ffrom=open(readfile,"r")
    hook=hookline
    if not hook:
        hook=''
    delayed=delay
    print('Define the Key to use by pressing it:')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


if __name__ == '__main__':
    import plac; plac.call(main)
