# requests模块应用测试2
# 构建爬取网页的通用代码框架：异常处理功能
# url: 链接

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 若状态码不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text

    except:
        return '产生异常'


web1 = 'http://www.baidu.com'
r2 = getHTMLText(web1)
print(r2)


