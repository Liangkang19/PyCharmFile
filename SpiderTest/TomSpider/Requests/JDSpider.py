# 京东商品页面爬虫：小米9手机
# https://item.jd.com/7437708.html

import requests
url = 'https://item.jd.com/7437708.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])  # 可指定返回内容的多少
except:
    print('爬取失败')


