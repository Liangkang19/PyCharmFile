# 亚马逊中文网爬虫

import requests
url = 'https://www.amazon.com/?language=zh_CN'
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:3000])
    print(r.request.headers)        # 识别访问类型为：浏览器/爬虫
except:
    print('爬取失败')





# url = 'https://www.amazon.com/?language=zh_CN'
# r = requests.get(url)
# print(r.status_code)              # 出现503错误编码
# print(r.encoding)
# r.encoding = r.apparent_encoding
# print(r.request.headers)              # 此时headers中出现python爬虫访问字样
# print(r.text)                         # 获得的相关信息可能不正确
#
# kv = {'user-agent': 'Mozilla/5.0'}    # 通过改变user-agent为相关浏览器，即模拟浏览器
# url = 'https://www.amazon.com/?language=zh_CN'
# r = requests.get(url, headers=kv)     # 添加headers参数
# print(r.status_code)                  # 成功出现200
# print(r.request.headers)              # 此时headers中出现Mozilla/5.0访问字样
# print(r.text)                         # 获得正确信息





