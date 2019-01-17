# -*- coding: utf-8 -*-

# Scrapy settings for qidian project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


#TODO 项目的名称
BOT_NAME = 'qidian'

#TODO 爬虫文件的路径
SPIDER_MODULES = ['qidian.spiders']
NEWSPIDER_MODULE = 'qidian.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent


#TODO 设置UA，模拟浏览器加载
#USER_AGENT = 'qidian (+http://www.yourdomain.com)'

# Obey robots.txt rules

#TODO 是否要遵循robot协议,默认为True（遵守）
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

#TODO scrapy发起请求的最大并发数量    默认为16
#CONCURRENT_REQUESTS = 32



# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

#TODO 下载延时，默认为0
DOWNLOAD_DELAY = 0
# The download delay setting will honor only one of:


#TODO 在每个域下允许发起请求的最大并发数    默认为8
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

#TODO 针对于每个IP，允许发起请求的并发数量   默认为0  IP不为0的情况下，优先级高于域  /  同事针对于IP而不是网站了
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)

#TODO 是否要携带cookie   默认为True/表示携带  BUG默认不追踪 COOKIES_DEBUG
#COOKIES_ENABLED = False



# Disable Telnet Console (enabled by default)

#TODO 是一个扩展插件，通过TELNT可以监听到当前爬虫的一些转台     默认开启True
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:

#TODO 请求头
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html

#TODO 爬虫中间件
#SPIDER_MIDDLEWARES = {
#    'qidian.middlewares.QidianSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html


#TODO 自定义下载中间见，在这里激活
DOWNLOADER_MIDDLEWARES = {
   # 'qidian.middlewares.QidianUserAgentDownloadmiddlerware': 543,
   # 'qidian.middlewares.QidianProxyDownloadMiddlerware': 544,
   # 'qidian.middlewares.SeleniumDownloadMiddlerware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html

#TODO EXTENSIONS扩展
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#TODO 激活管道

ITEM_PIPELINES = {
    # 'qidian.pipelines.QidianPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}


#TODO 动态设置下载延时

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#初始下载延时 5秒
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#最大的下载延时
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#发送到每个服务器的并行请求数量
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:

#TODO 是否开启自动限速的debug模式

# AUTOTHROTTLE_DEBUG = False




# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings


#数据缓存的扩展（默认关闭:False）
#HTTPCACHE_ENABLED = True
#设置缓存超时时间
#HTTPCACHE_EXPIRATION_SECS = 0
#设置缓存保存的路径
#HTTPCACHE_DIR = 'httpcache'
#缓存忽略的响应状态吗  比如为出现某个状态码不缓存
#HTTPCACHE_IGNORE_HTTP_CODES = []
#缓存的存储插件
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


"""将日志信息，保存到本地文件"""
# LOG_FILE = 'qilogfile.log'
# LOG_LEVEL = 'DEBUG'





"""配置数据库"""
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'qian_data'

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
]


#模拟一个代理池
PROXIES = [
    {'ip_port': '111.8.60.9:8123', 'user_pwd': 'user1:pass1'},
    {'ip_port': '101.71.27.120:80', 'user_pwd': 'user2:pass2'},
    {'ip_port': '122.96.59.104:80', 'user_pwd': None},
    {'ip_port': '122.224.249.122:8088', 'user_pwd': None},
]

#设置cookies
# COOKIES = {
#     {},
#     {},
#     {},
# }



#只是用scrapy的去重和保存功能，只需要修改settings.py文件中的设置信息
#爬虫文件不需要做修改

#这里是使用scrapy-redis自己实现的去重组件，不在使用scrapy框架内部的组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"


#使用scrapy-redis自己实现的调度器组件，不在使用scrapy框架内部的调度器组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#允许暂停和恢复,redis数据库中将会保存我们之前的请求记录
SCHEDULER_PERSIST = True

#request队列的三种模式

#scrapy.redis默认使用的队列模式，有自己的优先级(实质是使用了redis的有序集合)
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

#TODO 配置redis数据库信息

#指定redis数据库的host(公网ip)  TODO 要存储数据redis的主机ip
REDIS_HOST = '127.0.0.1'

#指定redis数据库的主机端口
REDIS_PORT = 6379
