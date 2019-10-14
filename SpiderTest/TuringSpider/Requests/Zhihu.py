import requests
from pyquery import PyQuery

url = 'https://www.zhihu.com/explore'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
html = r.text
doc = PyQuery(html)
text = doc('.ExploreSpecialCard-title')
items = text.items()
for item in items:
    result1 = item.text()
    result2 = item.attr('href')
    with open(file='zhihu_Ifo.txt', mode='a', encoding='utf8') as f:
        f.write('\n'.join([result1, 'http:/' + str(result2)]))
        f.write('\n' + '='*10 + '\n')

# f.write(result1 + ' ' + str(result2) + '\n')
