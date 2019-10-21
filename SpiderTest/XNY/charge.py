# 爬取新能源网--> 关键词:电动汽车充电
# 直接打印出数据
# 2019-10-17

import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

list1 = []
list2 = []
base_url1 = 'http://www.china-nengyuan.com/news/news_list.php?news_sort_id=6&keyword='
base_url2 = 'http://www.china-nengyuan.com'

# 'http://www.china-nengyuan.com/news/news_list.php?gopage=0&news_sort_id=6&keyword='
# 'http://www.china-nengyuan.com/news/news_list.php?gopage=1&news_sort_id=6&keyword='

goods = '电动汽车充电'
proxy = '51.68.172.7:3128'

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}

proxies1 = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
    }


def get_html_text(url, headers, proxies):
    """
        根据指定的url链接，爬取网页的html信息
        :param url: 链接
        :param headers: 请求头文件，用于伪装浏览器
        :param proxies: 代理IP，用于隐藏本机IP
    """
    try:
        r = requests.get(url=url, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('爬取成功！')
        return r.text
    except ConnectionError as e:
        print('ConnectionError', e.args)
    except HTTPError as e:
        print('HTTPError', e.args)


def parse_html_text(html, lista, listb):
    """
        根据指定的html文件，爬取主网页的标题信息和虚拟子链接
        :param html: html文件
        :param lista: 输入时为空列表，用于存储标题信息
        :param listb: 输入时为空列表，用于存储子链接
    """
    soup = BeautifulSoup(html, 'html.parser')
    for aa1 in soup.select('.member_tr_row td a'):
        lista.append(aa1.attrs['title'])
        listb.append(aa1.attrs['href'])


def get_child_html(url, listc, listd):
    """
        根据指定的虚拟子网页的url，爬取虚拟子网页的html信息，并通过调用parse_script_url()，得到真实的子链接
        :param url: 基础链接 base_url2
        :param listc: 存储子链接的列表
        :param listd: 存储标题
    """
    for i in range(len(listc)):
        child_url = url + listc[i]
        child_html = get_html_text(child_url, headers1, proxies1)
        result1 = '--->标题' + str(i + 1) + ': ' + listd[i] + '<---'
        save_to_file('\n' + result1 + '\n')
        parse_child_text(html=child_html)
        time.sleep(1)


def parse_child_text(html):
    """
        根据指定的html文件，爬取子网页的内容
        :param html: html文件
    """
    soup = BeautifulSoup(html, 'html.parser')

    for aa1 in soup.find_all(name='td', attrs={'class': "f14 news_link"}):
        for pp1 in aa1.find_all('p'):
            result2 = pp1.string
            save_to_file(result2)


def save_to_file(result):
    """
        将爬取的结果信息，存入本地的.txt文件中
        :param result: 爬取的结果信息
    """
    with open(file='Charge1.txt', mode='a', encoding='utf8') as f:
        f.write(str(result))


def main():
    """
        主函数，用于爬取一页主网页中的子网页信息
    """
    url1 = base_url1 + goods
    html1 = get_html_text(url=url1, headers=headers1, proxies=proxies1)
    parse_html_text(html=html1, lista=list1, listb=list2)
    get_child_html(url=base_url2, listc=list2, listd=list1)


if __name__ == '__main__':
    """
        用于启动主程序，遍历爬取主网页中的子网页信息   
    """
    main()



