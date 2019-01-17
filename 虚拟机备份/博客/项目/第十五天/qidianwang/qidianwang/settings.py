# -*- coding: utf-8 -*-

# Scrapy settings for qidianwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#项目名称
BOT_NAME = 'qidianwang'
#爬虫文件路径
SPIDER_MODULES = ['qidianwang.spiders']
NEWSPIDER_MODULE = 'qidianwang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#设置User-Agent:设置浏览器加载
# USER_AGENT = 'qidianwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
#是否尊守robot协议(默认为True遵守)
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#scrapy发起请求的最大并发数量 默认为16

# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs


#设置下载延迟默认为零
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:


#在每个域下允许发起请求的最大并发数 默认是8个
# CONCURRENT_REQUESTS_PER_DOMAIN = 16


#1针对于每个ip,允许发起请求的并发数量 默认为0
#2不为零的情况CONCURRENT_REQUESTS_PER_IP设置的优先级要比CONCURRENT_REQUESTS_PER_DOMAIN要高,
#3不为0的情况DOWNLDAD_DELAYD的下载延迟就会针对ip,而不是网站了
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#是否要携带cookies默认为True,表示携带cookies
# COOKIES_ENABLED = False
#COOKIES_DEBUG 默认为False表示不追踪cookies
# COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
#是一个扩展插件,可以通过ELNET监听到当前爬虫的一些状态
#默认开启的(True),
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#请求头的设置
DEFAULT_REQUEST_HEADERS = {
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#爬虫中间件
# SPIDER_MIDDLEWARES = {
#    'qidianwang.middlewares.QidianwangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#下载中间件(自定以的下载中键键需要在这里几号,后面的数字越小,优先级越高
DOWNLOADER_MIDDLEWARES = {
    'qidianwang.middlewares.QidianwangDownloaderMiddleware': 543,
                            # QdianUserAgenDownLoadmiddlerware
    # 'qidianwang.middlewares.QidianProxyDownloadMiddlerware': 544,
    # 'qidianwang.middlewares.SeleniumDownloadMiddlerWare':543,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS:扩展
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#激活管道(后面数字越小优先级越高
ITEM_PIPELINES = {
    'qidianwang.pipelines.QidianwangPipeline': 300,
}

#动态设置下载延时(自动限速的扩展)
#默认情况下是关闭的
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
#出事的下载延迟为5秒
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#发送到每个服务器并行请求的数量
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#是否开启自动限速的debug模式
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#数据缓存的宽展(默认情况下是关闭的:HTTPCACHE_ENABLED=False)
# HTTPCACHE_ENABLED = True
#设置缓存超时时间
# HTTPCACHE_EXPIRATION_SECS = 0
#设置缓存保持的路径
# HTTPCACHE_DIR = 'httpcache'
#缓存忽略的响应状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []
#存储插件
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#将log日志文件保存到本地文件
LOG_FILE= 'qdlogfile.log'
LOG_FILE = 'DEBUG'

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_DB = 'qidian1805'

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
]

# 在settings.py文件中模拟一个代理池(对于少量代理可以这么做)
PROXIES = [
    {'ip_port': '111.8.60.9:8123', 'user_pwd': 'user1:pass1'},
    {'ip_port': '101.71.27.120:80', 'user_pwd': 'user2:pass2'},
    {'ip_port': '122.96.59.104:80', 'user_pwd': None},
    {'ip_port': '122.224.249.122:8088', 'user_pwd': None},
]

#要实现只是使用scrapy的去重和保存功能,只需要修改settings.py文件中的设置信息爬虫文件不需要动
#这里是使用scrapy-redis自己实现的去重组件,不再使用scrapy框架内部的去重组件
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#这里是使用scrapy-redis自己实现的调度器组件,不再使用scrapy内部的调度器组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#允许暂停和恢复,redis数据库中将会保存我们之前的请求记录
SCHEDULER_PERSIST = True
#request队列的三种模式
#scrapy.redis默认使用的队列有自己的优先级(实质是使用了redis的有序集合)
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#使用了堆的形式(请求任务先进先出)
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#使用了栈的形式(请求任务先进后出)
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# 配置redis数据库信息
# 指定redis数据库的host(公网ip)(要存熟路redis的主机ip)
REDIS_HOST = '118.24.255.219'
#指定redis数据库端口(要存储数据redis的主机端口
REDIS_PORT = 6379
REDIS_ENCODING = 'utf8'
