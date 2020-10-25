from nerodia.browser import Browser

browser = Browser(browser='firefox')
browser.goto('https://myonlineportal.net/')

usrn = browser.text_field(name='username')
usrn.value = ''
pswd = browser.text_field(name='password')
pswd.value = ''
browser.button(value='Login').click()
browser.goto('https://myonlineportal.net/extend_account')
browser.button(value='Account verlängern!').click()
