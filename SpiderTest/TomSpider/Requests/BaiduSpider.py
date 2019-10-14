# 搜索引擎关键词提交爬虫:以Baidu和360为例
# 百度关键词接口：http://www.baidu.com/s?wd=keyword
# 360关键词接口: http://www.so.com/s?q=keyword

import requests

url = 'https://www.baidu.com/s'
keyword = 'python'
try:
    kv = {'wd': keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)          # 发给百度的request对应的url链接是什么？
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print('爬取失败')

