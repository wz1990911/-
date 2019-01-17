#创建一个项目
'1.scrapy startproject projectname(项目名称)'

#进入到spider文件夹下创建爬虫文件
'2.scrapy genspider 爬虫文件名称　网站的域'

#3.使用pycharm打开项目，设置虚拟环境

'''
scrapy项目的架构
chinaz:项目文件夹
    spider:爬虫文件(存放所有爬虫文件)
        zzw.py:爬虫文件(解析Response响应，提取目标数据和url)
    items.py:编写要爬取的字段
    middlewares.py:中间件(爬虫中间件，下载中间件)
    pipelines.py:数据管道(在这里做数据持久化)
    settings.py:设置文件(设置请求头，下载延时，是否遵守robot协议，激活管道文件...)
scrapy.cfg:配置文件，(部署项目的时候会使用到)
'''