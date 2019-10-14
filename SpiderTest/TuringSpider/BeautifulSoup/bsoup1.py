# BeautifulSoup库的使用

import requests
from bs4 import BeautifulSoup

url = 'http://maoyan.com/board/4'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}
r = requests.get(url=url, headers=headers)
demo = r.text
soup1 = BeautifulSoup(demo, 'html.parser')
print(list(soup1.li.parents)[0])
print(list(soup1.li.parents)[0]['class'])
# print(soup1.title)
# print(type(soup1.title))
# print(soup1.title.string)
# print(soup1.p)
# print(soup1.p.name)
# print(soup1.p['class'])
# print(soup1.ul.contents)
# print(soup1.ul.children)
# print(soup1.ul.descendants)
# print(soup1.a.parent)
# print(list(enumerate(soup1.li.parents)))
# print(soup1.li.parents)
# print('next', soup1.li.next_sibing)
# print('previous', soup1.li.previous_sibing)
# print('next', list(enumerate(soup1.li.next_sibing)))
# print('previous', list(enumerate(soup1.li.previous_sibing)))

# for i, child in enumerate(soup1.ul.children):
#     print(i, child)
#
# for i, child in enumerate(soup1.ul.descendants):
#     print(i, child)
