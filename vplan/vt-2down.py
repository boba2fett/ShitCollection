import re
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
            datum=datum.replace(".", "-")
            
            htmlDat = requests.get("http://www.gymnasium-mariengarden.de/vertretungsplan/plans.htm", headers=headers).text
            m = re.search('<td class=date align=right>(.*)<br />powered by sniessing</td>',htmlDat)
            creation = m.group(1)
            creation = creation.replace(".","-").replace(":","-")
            creaDate,creaTime =creation.split(" ")
            creaDate=datetime.strptime(creaDate, '%d-%m-%Y').strftime('%Y-%m-%d')
            dt_string=creaDate+"_"+creaTime
            
            if not os.path.exists('logExt/'+datum):
                os.mkdir('logExt/'+datum)
            print(dt_string)
            
            f = open('logExt/'+datum+'/'+dt_string+'.json', 'w')
            f.write(PlanData)
            f.close()
        
            planDate = plan["date"]
        time.sleep(250)

    except KeyboardInterrupt:
        exit()

    except:
        print("Fehler")












