#!/usr/bin/env python3
from nerodia.browser import Browser
import re

loginsite="https://mggym-borken.lms.schulon.org/login/index.php"


browser = Browser(browser='firefox')
browser.goto(loginsite)
usrn = browser.text_field(name="username")
usrn.value = ''
pswd = browser.text_field(name="password")
pswd.value = ''
browser.button(value='Login').click()

html=browser.html

#print(html:=browser.html)
matches=re.findall('<span.*>Meine Kurse<\/span>.*href="(https:\/\/mggym-borken.lms.schulon.org\/course\/view.php\?id=\d+)">.*href="(https:\/\/mggym-borken.lms.schulon.org\/course\/view.php\?id=\d+)">.*href="(https:\/\/mggym-borken.lms.schulon.org\/course\/view.php\?id=\d+)">',html)
kurse=list(matches[0])
#print(kurse)


for kurs in kurse:
    browser.goto(kurs)
    html=browser.html
    matches=re.findall('href="(https:\/\/mggym-borken\.lms\.schulon\.org\/mod\/resource\/view.php\?id=\d+)"><img src="https:\/\/mggym-borken\.lms\.schulon\.org\/theme\/image\.php\/classic\/core\/1587401819\/f\/pdf-24"',html)
    print(matches)

browser.close()
exit()
"Get all redirect links to a series (still have to extract manually  fromAndTo is an good option for this)"
base='https://s.to'
if base in site:
    site=site.replace(base,"")
if not site[-1]=="/":
    site=site+"/"
#print(base)
#print(site)

browser = Browser(browser='firefox')
browser.goto(base+site)
html=browser.html


matches=re.findall('<a (?:class="active" )?href="('+site+r'staffel-\d+)" title="Staffel \d+">\d+</a>',html)
#print(matches)
episodeRegex=re.compile(r'<a href="('+site+r'staffel-\d+/episode-\d+)" data-episode-id="\d*" title="Staffel \d+ Episode \d+" data-season-id="\d+">\d+</a>')
allepisodes=list()
for m in matches:
    browser.goto(base+m)
    html=browser.html
    episodes=episodeRegex.findall(html)
    allepisodes.extend(episodes)
#print(allepisodes)

VivoRegex=re.compile(r'<aclass="watchEpisode"itemprop="url"href="(/redirect/\d*)"target="_blank">\n<iclass="iconVivo"title="HosterVivo"></i>\n<h4>Vivo</h4>\n<divclass="hosterSiteVideoButton">Videoöffnen</div>')

vivolinks=list()

for e in allepisodes:
    browser.goto(base+e)
    html=browser.html
    html=html.replace(" ","")
    vivolink=VivoRegex.findall(html)
    vivolinks.append(vivolink[0])
#print(vivolinks)
for vl in vivolinks:
    print(base+vl)
browser.close()
