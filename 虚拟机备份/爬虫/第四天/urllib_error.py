# error:在请求过程中,会因为某些原因导致请求异常,
# 这些异常会导致我们的程序出现异常种植(崩溃
# 为了繁殖代码奔溃我本需要处理异常
from urllib import request, error


def check_url_error():
    url = 'https://www.badu.com/'
    """
    没有网络
    服务器连接失败
    找不到指定的服务器

    reason:返回错误原因
    """
    try:
        response = request.urlopen(url)
        print(response.status)
    except error.URLError as err:

        """
        1.[Errno -3] Temporary failure in name resolution:
        无法解析域名,即DNS解析配置出现问题
        2.[Errno -2] Name or service not known:
        未知的服务器,找不到服务器

        3.timed out
        请求超时
        """
        print(err.reason)


def check_http_error():
    '''
    一般人证错误,或者未发现资源
    httperror:返回属性
    code:返回请求状态吗
    reason:返回错误原因
    headers:发起请求的请求头

    '''
    url = 'http://www.eduxiao.com/wefawefawf'
    try:
        response = request.urlopen(url)
        print(response.status)
    except error.HTTPError as err:
        '''
        404
        Not Found
        Content-Length: 1308
        Content-Type: text/html
        Server: Microsoft-IIS/6.0
        X-Powered-By: ASP.NET
        Date: Tue, 20 Nov 2018 02:42:58 GMT
        Connection: close
        '''
        print(err.code)
        print(err.reason)
        print(err.headers)


#优化版本:因为HTTPerror是URLerror的子类
#所以通常情况下.线板段子异常


if __name__ == '__main__':
    # check_url_error()
    check_http_error()
