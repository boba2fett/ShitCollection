from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto('https://my.bplaced.net/')

usrn = browser.text_field(name="credentials_user")
usrn.value = ''
pswd = browser.text_field(name="credentials_pass")
pswd.value = ''
browser.button(value='Login').click()
