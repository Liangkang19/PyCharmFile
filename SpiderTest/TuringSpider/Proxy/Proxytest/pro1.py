# urllib代理测试
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = '119.76.132.239:8080'

proxy_handle = ProxyHandler({
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
    })

# 建立代理处理器
opener = build_opener(proxy_handle)
try:
    res = opener.open('http://httpbin.org/get')
    text = res.read().decode('utf-8')
    print(text)
    print('Request Successfully')
except URLError as e:
    print(e.reason)

