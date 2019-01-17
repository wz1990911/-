from selenium.common.exceptions import TimeoutException,NoSuchElementException,NoSuchFrameException

from selenium import webdriver


#浏览器驱动
driver = webdriver.Chrome(executable_path='/home/cui/桌面/driver/chromedriver')
#根据url打开页面
try:
    driver.get('https://www.wfawefawe.com/')
    driver.find_element_by_id('awfeawf')
    driver.switch_to_frame('afeae')
except TimeoutException as err:
    print(err,'超时')
except NoSuchElementException as err:
    print(err,'没有此节点')
except NoSuchFrameException as err:
    print('没有')






