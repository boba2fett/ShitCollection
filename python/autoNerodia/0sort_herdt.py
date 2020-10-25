#!/usr/bin/env python3
import time
import json
import os
import sys
from datetime import datetime

BASE_DIR="herdt/"
EXT=".pdf"

with open('0zuordnungen.json', 'r') as json_file:
        assignments = json.load(json_file)

for category in assignments:
        print(f"{category}")
        for filename in assignments[category]:
                bookname=assignments[category][filename]
                print(f"        {filename}: {bookname}")
                try:
                        print(f"                {BASE_DIR+filename+EXT}=> {BASE_DIR+filename+bookname+EXT}")
                        os.rename(BASE_DIR+filename+EXT,BASE_DIR+filename+bookname+EXT)
                except FileNotFoundError:
                        pass
