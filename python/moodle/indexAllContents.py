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
