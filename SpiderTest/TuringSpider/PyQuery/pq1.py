# pyquery中的CSS选择器

import requests
from pyquery import PyQuery

url = 'http://maoyan.com/board/4'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
html = r.text
doc = PyQuery(html)
docs = doc('.subnav .navbar li')     # .xxx -->选择属性值class="xxx"的所有元素
items1 = doc('.navbar')
list1 = items1.find('li')             # find()会将查找所有符合条件的子孙节点
list2 = items1.children('li')         # children()只查找所以符合条件的子节点
list3 = items1.parent()               # parent()查找父节点

list4 = doc('li').items()             # 使用items()将查找到的标签存入，遍历得到各个标签
# for li in list4:
#     print(li)

list5 = doc('.subnav .navbar li a')   # 查找class="subnav"-->class="navbar"
# print(list5)                        # -->所有li标签-->所有a标签
href = list5.attr('href')             # 用attr()查找标签中，xxx属性的元素值，只获得1个xxx的值
print(href)
# for hr in href.item():
#     print(hr.attr('href'))          # 当一个标签中，含有多个xxx属性，可用遍历方法获得每个属性值
text = list5.text()                   # 返回所有a标签的文本值，用空格分开
htmltext = list1.html()               # 返回第一个标签的HTML文本
print(text)
print(htmltext)

