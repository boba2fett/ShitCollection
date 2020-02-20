__version__="1.0.0"

import traceback

def update(dl_url, force_update=False):
    """
Attempts to download the update url in order to find if an update is needed.
If an update is needed, the current script is backed up and the update is
saved in its place.
"""
    import urllib
    import urllib.request
    import re
    import os,sys
    from subprocess import call
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
        
    # dl the first 256 bytes and parse it for version number
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
        print("Unable to parse version data")
        return

    if force_update:
        print("Forcing update, downloading version %s..." \
            % update_version)
    else:
        cmp_result = compare_versions(__version__, update_version)
        if cmp_result < 0:
            print("Newer version %s available, downloading..." % update_version)
        elif cmp_result > 0:
            print("Local version %s newer then available %s, not updating." \
                % (__version__, update_version))
            return
        else:
            print("Local version %s equal to available %s, not updating." \
                % (__version__, update_version))
            return

    # dl, backup, and save the updated script
    app_path = os.path.realpath(sys.argv[0])

    if not os.access(app_path, os.W_OK):
        print("Cannot update -- unable to write to %s" % app_path)

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
            # The header is improper or missing Content-Length, just download
            dl_file.write(http_stream.read())

        while total_size:
            chunk = http_stream.read(chunk_size)
            dl_file.write(chunk)
            bytes_so_far += len(chunk)

            if not chunk:
                break

            percent = float(bytes_so_far) / total_size
            percent = round(percent*100, 2)
            sys.stdout.write("Downloaded %d of %d bytes (%0.2f%%)\r" %
                (bytes_so_far, total_size, percent))

            if bytes_so_far >= total_size:
                sys.stdout.write('\n')

        http_stream.close()
        dl_file.close()
    except Exception as e:
        print(e)
        traceback.print_exc()
        return

    try:
        os.rename(app_path, backup_path)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return

    try:
        os.rename(dl_path, app_path)
    except Exception as e:
        print(e)
        traceback.print_exc()
        return

    try:
        import shutil
        shutil.copymode(backup_path, app_path)
    except Exception as e:
        print(e)
        traceback.print_exc()
        os.chmod(app_path, '0755')

    print("New version installed as %s" % app_path)
    print("(previous version backed up to %s)" % (backup_path))
    
    os.execl(sys.executable, os.path.abspath(file), *sys.argv)
    return
    
    
    
update('https://github.com/boba2fett/ShitCollection/raw/master/updater/up.py')
