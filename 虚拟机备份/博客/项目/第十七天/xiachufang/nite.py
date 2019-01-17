# 如果只使用实现通用爬虫的分布式爬取
# 第一步 需要改变setting.py文件,爬虫文件不需要做任何改动
# 修改settings.py文件
# 1
# #这里是使用scrapy-redis自己实现的去重组件,不再使用scrapy框架内部的去重组件
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 2
# #这里是使用scrapy-redis自己实现的去重组件,不再使用scrapy框架内部的去重组件
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 3
# #这里是使用scrapy-redis自己实现的调度器组件,不再使用scrapy内部的调度器组件
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 4
# #允许暂停和恢复,redis数据库中将会保存我们之前的请求记录
# SCHEDULER_PERSIST = True
# 5
#  'scrapy_redis.pipelines.RedisPipeline': 400,
# 6
# # 配置redis数据库信息
# # 指定redis数据库的host(公网ip)(要存熟路redis的主机ip)
# REDIS_HOST = ''
# #指定redis数据库端口(要存储数据redis的主机端口
# REDIS_PORT = 6379
# REDIS_ENCODING = 'utf-8'
#
# 第二部:修改爬虫文件
# 1修改爬虫文件继承的类:继承值RedisCrawlSpider
# 2去掉start_url参数,添加redis_key(从reids_数据库中的其实任务