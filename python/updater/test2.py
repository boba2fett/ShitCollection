import os
import sys

f = open("test.py", "w")
f.write("""
import traceback
try:
    print('es klappt!')
except:
    traceback.print_exc()
""")
f.close()

os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
