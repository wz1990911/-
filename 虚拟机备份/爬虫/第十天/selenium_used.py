#pip3 install selenium
#selenium 不自带浏览器,必须跟第三方浏览器结合使用

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#如何设置无头浏览器
opt = webdriver.ChromeOptions()
#设置为无头浏览器
opt.set_headless()

#创建一个浏览器驱动
chrome_driver = webdriver.Chrome(
    executable_path='/home/cui/桌面/driver/chromedriver',
)

# webdriver.PhantomJS 无头浏览器

chrome_driver.get('https://www.baidu.com/')


# chrome_driver.save_screenshot('baidu.png')
#获取页面源码是竞购浏览器渲染之后的结果
html_data = chrome_driver.page_source
print(html_data)

# 模拟用户操作在搜索栏输入文字
chrome_driver.find_element_by_id('kw').send_keys('邢凯')
#点击按钮
chrome_driver.find_element_by_id('su').click()
time.sleep(3)
#隐士等待:当我们寻找节点的时候有时候页面可能没有加载出来设置隐士等待,没找到的话就会等一会寻找,如果在设定时间还没有找到就会异常
chrome_driver.implicitly_wait(10)
# #点击下一页
# chrome_driver.find_element_by_class_name('n').click()
# time.sleep(3)
#根据文字寻找
# chrome_driver.find_element_by_link_text('下一页>').click()
chrome_driver.find_element_by_id('kw').clear()
chrome_driver.find_element_by_id('kw').send_keys('邢凯的媳妇是谁')
'''
# Keys.RETURN模拟键盘回车
chrome_driver.find_element_by_id('su').send_keys(Keys.RETURN)
#通过节点的那么属性查找节点
chrome_driver.find_element_by_class_name()
#通过节点的class_name找到对应节点
chrome_driver.find_element_by_class_name()
#通过css选择器查找对应的节点
chrome_driver.find_element_by_css_selector()
#通过链接躲在标签部分文字找到节点
chrome_driver.find_element_by_partial_link_text()
'''
print(chrome_driver.find_element_by_id('su').get_attribute('value'))

print(chrome_driver.find_element_by_class_name('n').text)


#获取cookies
# cookies = chrome_driver.get_cookie()
#可以获取当前url
cur_url = chrome_driver.current_url
print(cur_url)

#回退
chrome_driver.back()
#前进
chrome_driver.forward()
#关闭浏览器(只有一个页面会退出多个页面会关闭当前页面_
chrome_driver.close()
#退出浏览器
chrome_driver.quit()