# requests代理测试

import requests
from requests.exceptions import ConnectionError

url = 'http://httpbin.org/get'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
proxy = '186.226.183.170:54704'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
    }

try:
    r = requests.get(url=url, headers=headers, proxies=proxies, timeout=10)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except ConnectionError as e:
    print('Error', e.args)
