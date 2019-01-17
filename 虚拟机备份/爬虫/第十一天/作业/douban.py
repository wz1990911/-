from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient

class douyu_spider(object):

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='/home/cui/桌面/driver/chromedriver'
        )

    def get_list_data(self):
        self.driver.get('https://movie.douban.com/')
        self.driver.find_element_by_xpath('//input[@id="inp-query"]').send_keys('范冰冰')
        self.driver.find_element_by_xpath('//div[@class="inp-btn"]').click()

        self.dingqiu()

    def dingqiu(self):

        html = self.driver.find_elements_by_xpath('//div[@class="item-root"]')

        for i in html:
            zidian = {}
            try:
                zidian['封面'] = i.find_element_by_xpath('./a[@class="cover-link"]/img').get_attribute('src')
                zidian['名字'] = i.find_element_by_xpath('./a[@class="cover-link"]/img').get_attribute('alt')
                zidian['评分'] = i.find_element_by_xpath('.//span[@class="rating_nums"]').text
                zidian['评价'] = i.find_element_by_xpath('.//span[@class="pl"]').text
                zidian['分类'] = i.find_element_by_xpath('.//div[@class="detail"]/div[3]').text
                zidian['演员'] = i.find_element_by_xpath('.//div[@class="detail"]/div[4]').text
                self.chucun(zidian)
            except:
                print('错误')
        element = self.driver.find_element_by_class_name('next')
        if element:
            element.click()
            self.dingqiu()
        else:
            print('没有下一页了')
            self.driver.quit()
    def chucun(self,zidian):
        try:
            client = MongoClient(host='localhost', port=27017)
            db = client.douban
            db.douban.insert_one(zidian)
            print(zidian['名字'] + '写入成功')
        except:
            print(zidian['名字'] + '写入失败')


if __name__ == '__main__':
    douban = douyu_spider()
    douban.get_list_data()