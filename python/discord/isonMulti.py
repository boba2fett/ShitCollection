#!/usr/bin/env python3
import requests
import time
import json
import os
import sys
from datetime import datetime
from pyfcm import FCMNotification

push_service = FCMNotification(
    api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")
registration_ids = [
    # "dSvcsDop4ek:APA91bFcfxJak8NLbyxjpXavu3RLbf28jNLRRcAcTTN7_dzg-MS8rzN3uRsPvMgpmPNvpJCaRIFMOliUDX169uf3cH2V7isYYMa0F6Hn5VZRunVhz_ZJBUot5m9V2HotGtbBxtAULUvM",
    "fg09UzZglnc:APA91bHThBBv5LA-VmM3xrU1NkfCMqyZ5cR9_50PoiG_MNXpmJdoQ2XhX2s9hiFFQZnHirwLq032YH0HaTy_EBBX7YfKwiUr1disox8had4zU9Lo1DO9KP1PiExiYP9cMCd6LSNLdmP9"
]
headers = {
    'User-Agent': 'Mozilla/51.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

names = sys.argv[1::]
oldStates = {name: False for name in names} # False means offline

while True:
    try:
        dcData = requests.get(
            "https://discordapp.com/api/guilds/486990202154254376/embed.json", headers=headers).text # link is under server settings widgets or similar
        dc = json.loads(dcData)
        on = [x['username'] for x in dc['members']]
        states = {name: name in on for name in names}
        for name in names:
            if states[name] != oldStates[name]: # if online state changed
                try:
                    message_title = '[' + \
                        datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+']'
                    message_body = name
                    message_body += " geht on" if not oldStates[name] else " geht off"
                    result = push_service.notify_multiple_devices(
                        registration_ids=registration_ids, message_title=message_title, message_body=message_body)
                    print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +
                          '] Online Message gesendet', flush=True)

                except Exception as e:
                    print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +
                          '] Online Message failed because of \n'+str(e)+'\n', flush=True)
                oldStates[name] = states[name]
        time.sleep(250)
    except KeyboardInterrupt:
        exit()

    except Exception as e:
        try:
            message_title = '[' + \
                datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+']'
            message_body = str(e)
            result = push_service.notify_multiple_devices(
                registration_ids=registration_ids, message_title=message_title, message_body=message_body)
            print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +
                  '] Fehler Message gesendet für \n'+str(e)+'\n', flush=True)

        except Exception as e2:
            print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S") +
                  '] Fehler Message failed because of \n'+str(e2)+' für \n'+str(e)+'\n', flush=True)

        time.sleep(600)
