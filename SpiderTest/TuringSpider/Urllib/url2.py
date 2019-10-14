# 使用Request构造访问

from urllib import request, parse

url1 = 'http://httpbin.org/post'
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Host': 'httpbin.org'
}
dict1 = {'name': 'address'}
data1 = parse.urlencode(dict1)
data2 = bytes(data1, encoding='utf-8')
req = request.Request(url=url1, data=data2, headers=headers1, method='POST')
res = request.urlopen(req)
text = res.read().decode('utf-8')
print(text)
