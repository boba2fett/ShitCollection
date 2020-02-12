import re
import requests
import time
import json
import os, sys
from datetime import datetime
import smtplib


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
            print('['+dt_string+'] neuer Plan für den '+datum)
            
            f = open('logVplan/'+datum+'/'+dt_string+'.json', 'w')
            f.write(PlanData)
            f.close()
        
            planBefore = plan
            
            
            
        
        moniDat= requests.get("https://www.gymnasium-mariengarden.de/vertretungsplan/monitore/custom.html", headers=headers).text
        if moniBefore != moniDat:
            moniBefore=moniDat
            m = re.search('<span style="background-color: #ced4d9; color: #e03e2d;">.*(\d\d\d\d) \((.*)\)</span></h2>',moniDat)
            forYear = m.group(1)
            forKW=m.group(2).replace(".","-")
            forDate=forYear+"_"+forKW
            
            fromDate=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            if not os.path.exists('logMoni/'+datum):
                os.mkdir('logMoni/'+datum)
            print('['+fromDate+'] neuer Monitor für '+forDate)
            
            f = open('logMoni/'+forDate+'/'+fromDate+'.html', 'w')
            f.write(moniDat)
            f.close()
            
        
        time.sleep(250)

    except KeyboardInterrupt:
        exit()

    except, e:
        sender = 'fehler@datensammler.com'
        receivers = ['boba2002fett@gmail.com']

        message = """From: Datensammelfehler <fehler@datensammler.com>
        To: Boba <boba2002fett@gmail.com>
        Subject: Error Mail
        
        {0}
        """
        
        message=message.format(str(e))

        try:
           smtpObj = smtplib.SMTP('localhost')
           smtpObj.sendmail(sender, receivers, message)         
           print("Successfully sent ERROR email for\n"+str(e)+"\n")
        except SMTPException:
           print("Error: unable to send ERROR email for\n"+str(e)+"\n")

