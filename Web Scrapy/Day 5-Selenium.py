from selenium import webdriver
url = 'https://mail.163.com/'
browser = webdriver.Chrome()
browser.get(url)

iframe = browser.find_element_by_id('x-URS-iframe1551786034481.7268')
browser.switch_to.frame(iframe)

iframe = browser.find_element_by_xpath('//div/iframe')
    browser.switch_to.frame(iframe)
    browser.find_element_by_name('email')
    browser.find_element_by_name('email').send_keys(id) #输入账号
    browser.find_element_by_name('password').clear()
    browser.find_element_by_name('password').send_keys(passwd) # 输入密码
    browser.find_element_by_id('dologin').click() # 点击登录
