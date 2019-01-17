# 这个模块用来获取鼠标的点击操作
from selenium.webdriver import  ActionChains
from selenium import  webdriver
import time


#构建一个驱动
driver = webdriver.Chrome(executable_path='/home/cui/桌面/driver/chromedriver')

driver.get('https://www.baidu.com')
#获取a标签
a_action = driver.find_element_by_xpath('//div[@id="u1"]/a[3]')
#将鼠标移动到a标签上
ActionChains(driver).move_to_element(a_action).perform()
# #单击
# ActionChains(driver).move_to_element(a_action).click(a_action).perform()
# #双击
# ActionChains(driver).move_to_element(a_action).double_click(a_action).perform()
# a_action_1 = driver.find_element_by_xpath('//div[@id="u1"]/a[5]')
# ActionChains(driver).drag_and_drop(a_action,a_action_1).perform()
#切换到系统的提示框
# alter = driver.switch_to_alert()
#执行js代码,重新打开一个窗口
js = 'window.open("http://www.douban.com/")'
driver.execute_script(js)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])

#切换到子页面iframe
fram = driver.switch_to_frame('loginIframe')





