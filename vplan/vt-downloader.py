import requests
import time
import json
import os, sys
from datetime import datetime

planDate = ""

while True:
    try:
        headers = {'User-Agent': 'Mozilla/51.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        PlanData = requests.get("http://gymnasium-mariengarden.de/vertretungsplan/PlanData.json", headers=headers).text
        plan = json.loads(PlanData)
        
        if planDate != plan["date"]:
            datum, version = plan["date"].split(" ")
            if not os.path.exists('log/'+datum.replace(".", "-")):
                os.mkdir('log/'+datum.replace(".", "-"))
            dt_string = datetime.now().strftime("%H-%M-%S")
            print(dt_string)
            f = open('log/'+datum.replace(".", "-")+'/'+dt_string+'.json', 'w')
            f.write(PlanData)
            f.close()
        
            planDate = plan["date"]
        time.sleep(250)

    except KeyboardInterrupt:
        exit()

    except:
        print("Fehler")
