import re
import requests
import time
import json
import os, sys
from datetime import datetime
from pyfcm import FCMNotification

planBefore = ""
headers = {'User-Agent': 'Mozilla/51.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
moniBefore= ""

while True:
    try:
        PlanData = requests.get("http://gymnasium-mariengarden.de/vertretungsplan/PlanData.json", headers=headers).text
        plan = json.loads(PlanData)
        
        if planBefore != plan:
            datum, version = plan["date"].split(" ")
            datum=datum.replace(".", "-")
            datum=datetime.strptime(datum, '%d-%m-%Y').strftime('%Y-%m-%d')
            
            htmlDat = requests.get("http://www.gymnasium-mariengarden.de/vertretungsplan/plans.htm", headers=headers).text
            m = re.search('<td class=date align=right>(.*)<br />powered by sniessing</td>',htmlDat)
            creation = m.group(1)
            creation = creation.replace(".","-").replace(":","-")
            creaDate,creaTime =creation.split(" ")
            creaDate=datetime.strptime(creaDate, '%d-%m-%Y').strftime('%Y-%m-%d')
            dt_string=creaDate+"_"+creaTime
            
            if not os.path.exists('logVplan/'+datum):
                os.mkdir('logVplan/'+datum)
            print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'] neuer Plan vom '+dt_string+' für den '+datum)
            
            f = open('logVplan/'+datum+'/'+dt_string+'.json', 'w')
            f.write(PlanData)
            f.close()
        
            planBefore = plan
            
            
            
        
        moniDat= requests.get("https://www.gymnasium-mariengarden.de/vertretungsplan/monitore/custom.html", headers=headers).text
        if moniBefore != moniDat:
            moniBefore=moniDat
            m = re.search('<span style="background-color: #ced4d9; color: #e03e2d;">.*(\d\d\d\d) \((.*)\)</span></h2>',moniDat)
            forYear = m.group(1)
            forKW=m.group(2).replace(".","-").replace(" ","")
            forDate=forYear+"_"+forKW
            
            fromDate=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            if not os.path.exists('logMoni/'+forDate):
                os.mkdir('logMoni/'+forDate)
            print('['+fromDate+'] neuer Monitor für '+forDate)
            
            f = open('logMoni/'+forDate+'/'+fromDate+'.html', 'w')
            f.write(moniDat)
            f.close()
            
        
        time.sleep(250)

    except KeyboardInterrupt:
        exit()

    except Exception as e:
        try:
            push_service = FCMNotification(api_key="AAAAOL_f7Vw:APA91bHx4r3FM3rH2RxU2JtjoMRMm8At-c9XGrUnxpp6BCHtQLup1uvjAzIifOBAMMqCDOi_Z0O6wgqYGMtVJdt4EUdVzBXiUmpP_kTJRWB_9TmJBTp2II3tELBvSBhQvxMZxxLYP_Xu")

            registration_ids = [
            #"czKru1lRZX4:APA91bE3VVc_iwDxTaYVtHljlA1OQebkZHyCGhKjwb-n9AeNwXGwMQOd71kHmwK20hFB5fDQCSfSRc-piirHH-swvYSrcURiMmLLXMq3EC3TSGW6cSstqPqpeNVKSi3hwOsQwGmN1SsM",
            "fg09UzZglnc:APA91bHThBBv5LA-VmM3xrU1NkfCMqyZ5cR9_50PoiG_MNXpmJdoQ2XhX2s9hiFFQZnHirwLq032YH0HaTy_EBBX7YfKwiUr1disox8had4zU9Lo1DO9KP1PiExiYP9cMCd6LSNLdmP9"
                    ]
            message_title = '['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+']'
            message_body = str(e)
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
            print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'] Fehler Message gesendet für \n'+str(e)+'\n')
            
        except Exception as e2:
            print('['+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'] Fehler Message failed because of \n'+str(e2)+' für \n'+str(e)+'\n')
        
        time.sleep(600)
        
        
       
