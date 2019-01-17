from selenium import webdriver
#负责循环等待
from selenium.webdriver.support.ui import WebDriverWait

#以什么方式寻找节点
from selenium.webdriver.common.by import By
#添加条件模块
from selenium.webdriver.support import expected_conditions as EC
#显示扥带:同样可以指定一根等待时间,不过跟家灵活,可以制定一个最长等待时间
#如果在最长时间没找到节点就会抛出异常
driver = webdriver.Chrome(executable_path='/home/cui/桌面/driver/chromedriver')

driver.get('https://www.douban.com/')
try:
    #寻找节点
    element = WebDriverWait(driver,10).until(
        #添加寻找节点的条件
        EC.presence_of_element_located((By.ID,'anony-time'))
    )
    print('节点找到了')
    print('element')
except Exception as err:
    print('节点未找到')
    print(err)


