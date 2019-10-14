# 代理: ProxyHandle

from urllib.error import URLError
from urllib.request import build_opener
from urllib.request import ProxyHandler

# 添加代理链接
proxy_handle = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})
# 建立代理处理器
opener = build_opener(proxy_handle)
try:
    res = opener.open('http://www.baidu.com')
    text = res.read().decode('utf-8')
    print(text)
    print('Request Successfully')
except URLError as e:
    print(e.reason)
