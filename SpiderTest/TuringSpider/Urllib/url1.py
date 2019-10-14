# urllib库的基本使用
# request ：http请求模块
# parse   ：url处理模块
# urlopen ：获得相关网页信息

import urllib.request
import urllib.parse
import urllib.error
import socket

try:
    r = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    text = r.read().decode('utf-8')
    print(text)

except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TimeoutError')

# print(type(r))
# print(r.status)
# print(r.getheaders())
# print(r.getheader('Server'))
# data = urllib.parse.urlencode({'word': 'hello'})  # 上传的数据流
# transdata = bytes(data, encoding='utf-8')         # 转码的数据流
# r = urllib.request.urlopen('http://httpbin.org/post', data=transdata, timeout=0.1)
# text = r.read().decode('utf-8')
# print(text)
