from selenium import webdriver
from lxml import etree

class douyu_spider(object):

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='/home/cui/桌面/driver/chromedriver'
        )

    def get_list_data(self):
        #打开斗鱼的页面
        self.driver.get('https://www.douyu.com/directory/all')
        # #获取页面的源码：
        # html = self.driver.page_source
        # #可以使用xpath做解析
        # if html:
        #     html_element = etree.HTML(html)
        self.get_video_data()


    def get_video_data(self):

        video_lis = self.driver.find_elements_by_xpath('//ul[@id="live-list-contentbox"]/li')

        for li in video_lis:
            video_dict = {}
            video_dict['title'] = li.find_element_by_xpath('.//h3[@class="ellipsis"]').text
            video_dict['image_cover'] = li.find_element_by_xpath('.//span[@class="imgbox"]/img').get_attribute('data-or')
            try:
                video_dict['author'] = li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
            except:
                video_dict['author'] = '暂无'

            try:
                video_dict['hotnum'] = li.find_element_by_xpath('.//span[@class="dy-num fr"]').text
            except:
                video_dict['hotnum'] =0
            self.save_data_to_db(video_dict)

        # 获取下一页
        element = self.driver.find_element_by_class_name('shark-pager-next')
        if element:
            element.click()
            self.get_video_data()
        else:
            print('没有下一页了')
            self.driver.quit()

    def save_data_to_db(self,data):
        print('在这里做数据的持久化')
        print(data)

if __name__ == '__main__':

    spider = douyu_spider()
    spider.get_list_data()




