# 爬取软科中国大学排名
# http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html

import requests
import bs4
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def getHTMLText(url):                        # 获取网页信息
    try:
        r = requests.get(url, timeout=30)    # 爬取信息
        r.raise_for_status()                 # 判断是否爬取成功：200
        r.encoding = r.apparent_encoding     # 转码
        print('爬取成功！')
        return r.text                        # 将爬取的网页信息返回

    except RequestException:
        print('爬取失败！')
        return None                          # 爬取失败后返回空


def fillUnivList(ulist, html):       # 提取网页信息中的大学排名信息到合适的数据结构中
    soup = BeautifulSoup(html, 'html.parser')  # 将html中的数据打包，采用parser解析器
    # 大学排名信息在tbody>>tr>>td中
    for tr in soup.find('tbody').children:     # 将soup中的tbody中的子标签tr提取出来
        if isinstance(tr, bs4.element.Tag):    # 判断tr是否都为Tag标签类型
            tds = tr.find_all('td')            # 将tr标签中的子标签td存为列表类型
            ulist.append([tds[0].string, tds[1].string, tds[3].string])  # 将td标签中的字符信息存入ulist列表中
    pass


def printUnivList(ulist, num):          # 利用数据结构中的数据输出结果
    print('{:^10}\t{:^10}\t{:^10}\t'.format('排名', '学校名称', '总分'))  # 打印出表头
    for i in range(num):
        u = ulist[i]                    # 取出ulist列表中的信息
        print('{:^10}\t{:^10}\t{:^10}\t'.format(u[0], u[1], u[2]))  # 将信息打印出来
    print('Suc' + str(num))             # 程序运行结束标志


def univmain():                    # 创建主函数
    uinfo = []                     # 创建一个名为unifo的空列表
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)        # 爬取网页信息到html中
    fillUnivList(uinfo, html)      # 提取html中的大学排名信息，放入unifo中
    printUnivList(uinfo, 30)       # 将unifo中的大学排名信息打印出来


univmain()
