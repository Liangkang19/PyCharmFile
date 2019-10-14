# BeautifulSoup库的使用
# find_all(name, attrs, recursive, text)

import requests
from bs4 import BeautifulSoup

url = 'http://maoyan.com/board/4'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}
r = requests.get(url=url, headers=headers)
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')

print(soup.find_all(attrs={'class': 'releasetime'}))   # 使用attrs，找出包含class中属性值的标签
print(soup.find_all(class_="releasetime"))             # 找出所有包含class中属性值的标签，为了区别，使用class_
# print(soup.find_all(name='ul'))          # 找出所有<ul>标签下的信息
# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))        # 找出每一个<ul>标签的子标签<li>的信息
