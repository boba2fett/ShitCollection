from nerodia.browser import Browser
import re
from selenium import webdriver
import json

BASE="https://herdt-campus.com"



fp = webdriver.FirefoxProfile('/home/bf/.mozilla/firefox/a67xxtyb.auto')
driver = webdriver.Firefox(fp)


#browser = Browser(browser='firefox')

browser = Browser(driver)

browser.goto('https://bk-ostvest.lms.schulon.org/mod/url/view.php?id=16833')

usrn = browser.text_field(name='username')
usrn.value = ''
pswd = browser.text_field(name='password')
pswd.value = ''
browser.button(value='Login').click()

browser.button(value='Ich stimme zu!').click()

katalog=re.findall(r'<a class="catalog-nav-link" href="(\/category\/herdt-themen\/[\w\/\- ]*)">[\w\/\- ]*<\/a>',browser.html)

categorieDict=dict()

for category in katalog:
    #browser.goto(category)

    site=0

    dic=dict()

    while True:
        browser.goto(BASE+f"{category}?page={site}")
        books=re.findall(r'<a class="h4 product-title-custom" href="(\/product\/[\w\/\- ]*)">[\w\/\- ]*<\/a>',browser.html)

        for book in books:
            browser.goto(BASE+book)
            #browser.button(value='Download').click()
            #print(book)
            dic[book.replace("/product/","")]=re.findall(r'<h1 class="mb-3">([\w\/\- \(\)]*)</h1>',browser.html)[0]


        sites=re.findall(r'<a class="page-link" href="\/category\/herdt-themen\/programmierungweb\?page=(\d+)" data-page="\d+">\d+<\/a>',browser.html)
        if not any(s > site for s in sites):
            break
        site+=1

    categorieDict[category.replace("/category/herdt-themen/","")]=dic

print(json.dumps(categorieDict, indent=4, sort_keys=True))

#<h1 class="mb-3">Windows 10 (1903) Grundkurs kompakt</h1>

#<a class="page-link" href="/category/herdt-themen/programmierungweb?page=2" data-page="1">2</a>

#<a class="h4 product-title-custom" href="/product/K-W10-G-1903">Windows 10 (1903) Grundkurs kompakt</a>

#<a class="catalog-nav-link" href="/category/herdt-themen/windowsoffice">Windows</a>
