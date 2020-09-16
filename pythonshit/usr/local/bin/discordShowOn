#!/usr/bin/env python3
import requests
import time
import json
import os, sys
from datetime import datetime
headers = {'User-Agent': 'Mozilla/51.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}


dcData = requests.get("https://discordapp.com/api/guilds/486990202154254376/embed.json", headers=headers).text
dc = json.loads(dcData)
on=[x['username'] for x in dc['members']]
for name in on:
    print(name)