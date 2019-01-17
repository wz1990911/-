from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#创建一个浏览器驱动
chrome_driver = webdriver.Chrome(
    executable_path='/home/cui/桌面/driver/chromedriver',
)
chrome_driver.get('https://github.com/login?return_to=%2Ffeatures%2Fproject-management')
chrome_driver.find_element_by_id('login_field').send_keys('2905682123@qq.com')
chrome_driver.find_element_by_id('password').send_keys('wz990911')
time.sleep(3)
chrome_driver.find_element_by_xpath('//input[@name="commit"]').click()