#!/usr/bin/env python3
import sys, os
import webbrowser as wb
from urllib.parse import urlencode

try:
    a=int("a")
except Exception as e:
    wb.open_new_tab('https://duckduckgo.com/?t=lm&'+urlencode(dict(q=str(e)))+'&ia=web')
