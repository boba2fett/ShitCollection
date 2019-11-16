import urllib.request
import json
import time


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,}
url='https://www.gymnasium-mariengarden.de/vertretungsplan/PlanData.json'
date='dummy'
while True:
    response = urllib.request.urlopen(urllib.request.Request(url,None,headers))
    responsejson=response.read()
    plandata = json.loads(responsejson)
    if plandata["date"] != date:
        date=plandata["date"]
        print("new Version")
    time.sleep(60*5)
