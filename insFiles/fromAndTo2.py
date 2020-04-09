#!/usr/bin/env python3
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys, os
import time

CRED = '\033[91m'
CEND = '\033[0m'

debug=False
Fto=''
Ffrom=''
usekey=''
last_line=''
last_read=''
pyperclip.copy('')
hook=''
delayed=False
#keyboardController = Controller()

def copyToFile():
    global Fto, Ffrom, last_line, hook, keyboardController, delayed
    try:
        keyboardController = Controller()
        keyboardController.press(Key.ctrl.value)
        keyboardController.press('c')
        keyboardController.release('c')
        keyboardController.release(Key.ctrl.value)
        if delayed:
            if debug:
            	print('wait')
            time.sleep(0.7)
        else:
            time.sleep(0.4)
        pp=pyperclip.paste()
        if pp!=last_line and hook in pp:
            if debug:
            	print('Write: '+pp)
            Fto.write(pp+'\n')
            last_line=pp
            return True
        else:
            if debug:
            	print('Same as last or '+hook+' not inside')
            return False
    except:
        print(CRED+'failed to press sth'+CEND)
        Fto.close()
        Ffrom.close()
        exit()


def pasteFromFile():
    global Fto, Ffrom, delayed, last_read
    line = Ffrom.readline()
    if not line:
        print('Reached EOF')
        Ffrom.close()
        return False
    else:
        last_read=line
        pyperclip.copy(line.strip())
        if debug:
        	print('Read: '+pyperclip.paste())
        if delayed:
            if debug:
            	print('wait')
            time.sleep(0.7)
        else:
            time.sleep(0.4)
        try:
            keyboardController = Controller()
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


def stop():
    global last_read, Fto, Ffrom
    remaining=Ffrom.name+".remaining"
    while os.path.isfile(remaining):
        remaining+=".Kek"
    Fremain=open(remaining,"w")
    lines=Ffrom.readlines()
    Fremain.write(last_read+''.join(lines))
    Fremain.close()
    Fto.close()
    Ffrom.close()
    print("Pressed Esc wrote remaining lines to: "+remaining)
    return False

def on_press(key):
    global usekey, last_line, Ffrom, Fto
    if key == Key.esc:
        return stop()# stop listener
    if usekey=='':# very first time
        usekey=key
        print('Will use: '+str(usekey))
    elif key==usekey:
        if debug:
        	print('UseKey pressed: ' + str(key))
        if pyperclip.paste()=='': # first time
            pasteFromFile()
            return not Ffrom.closed
        else:
            if copyToFile():
                return pasteFromFile()


def main(readfile,writefile,hookline: ('search for occurence of string', 'option', 's'),delay: ('make a bigger delay before using clipboard', 'flag', 'd'),verbose: ('verbose output', 'flag', 'v')):
    "Insert line by line in a file from a GUI by just pressing a key (ESC exits everytime)"
    global Fto, hook, Ffrom, delayed, debug
    Fto=open(writefile,"w")
    Ffrom=open(readfile,"r")
    hook=hookline
    debug=verbose
    if not hook:
        hook=''
    delayed=delay
    print('Define the Key to use by pressing it:')
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


if __name__ == '__main__':
    import plac; plac.call(main)
