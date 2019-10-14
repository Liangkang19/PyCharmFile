# BeautifulSoup库的测试
# BeautifulSoup库是解析，遍历，维护“标签树”的功能库
# 标签树：<html>
#           <body>
#                <p class="title"> ... </p>
#           </body>
#        </html>
# 键值对：key:value
# 例: 'name': '老四'

import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup1 = BeautifulSoup(demo, 'html.parser')    # 参数一：需要解析的html格式的信息
# print(soup1.prettify())                     # 参数二：解析器
taga = soup1.a                                # 获得a标签信息
tagp = soup1.p                                # 获得b标签信息
print(taga.attrs)
print(taga.attrs['class'])
print(taga.attrs['href'])
print(taga.string)
print(tagp.string)
# print(soup1.title)
# print(soup1.a)
# print(soup1.a.name)
# print(soup1.a.parent.name)
# print(soup1.a.parent.parent.name)



