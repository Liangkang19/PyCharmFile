# parse 解析方式的使用

from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlsplit
from urllib.parse import urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode
from urllib.parse import parse_qs
from urllib.parse import parse_qsl
from urllib.parse import quote
from urllib.parse import unquote

result1 = urlparse('http://www.baidu.com/index.html;user?id=8#comment')
print(type(result1), result1)
data1 = ['http', 'www.baidu.com', 'index.html', 'user', 'id=8', 'comment']
url1 = urlunparse(data1)
print(url1)
result2 = urlsplit('http://www.baidu.com/index.html;user?id=8#comment')
print(result2)
data2 = ['http', 'www.baidu.com', 'index.html', 'user', 'id=8']
url2 = urlunsplit(data2)
print(url2)
url3 = urljoin('http://www.baidu.com', 'index.html')
print(url3)
params1 = {
    'name': 'laosi',
    'age': '35'
}
base_url = 'http://www.baidu.com?'
url4 = base_url + urlencode(params1)
print(url4)
data3 = 'name=laosi&age=35'
params2 = parse_qs(data3)
print(params2)
params3 = parse_qsl(data3)
print(params3)
keyword = '老四'
search_url = 'http://www.baidu.com/s?wd='
url5 = search_url + quote(keyword)
print(url5)
url6 = unquote(url5)
print(url6)
