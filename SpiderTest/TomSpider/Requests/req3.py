# requests库中的request模块的使用
# url: 链接
# Robots协议：允许爬取的数据信息目录与不允许爬取的数据信息目录
# Robots协议查看案例
# http://www.baidu.com/robots.txt
# http://news.sina.com.cn/robots.txt
# http://www.qq.com/robots.txt
# http://news.qq.com/robots.txt
# http://www.moe.edu.cn/robots.txt


import requests
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://python123.io/ws', params=payload)
print(r.url)
r = requests.request('PUT', 'http://python123.io/ws', data=payload)
r = requests.request('POST', 'http://python123.io/ws', json=payload)
hd = {'user-agent': 'Chrome/'}
r = requests.request('POST', 'http://python123.io/ws', headers=hd)
fs = {'files': open('data.xlsx', 'rb')}
r = requests.request('POST', 'http://python123.io/ws', files=fs)
r = requests.request('GET', 'http://python123.io/ws', timeout=10)  # 单位为s
pxs = {'http': 'http://user:pass@10.10.1:1234', 'https': 'http://user:pass@10.10.1:1234'}
r = requests.request('GET', 'http://baidu.com', proxies=pxs)


