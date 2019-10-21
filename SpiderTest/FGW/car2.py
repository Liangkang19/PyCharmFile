# 爬取发改委网站--> 关键词:电动汽车
# 数据存储在.txt文件中
# 2019-10-9

import re
import time
import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

base_url1 = 'http://118.178.151.173/s?q=1&qt='
base_url2 = 'http://118.178.151.173/'
goods = '电动汽车充电'
params = '&pageSize=10&database=all&siteCode=bm04000007&docQt=&page='

headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
}
proxy = '51.68.172.7:3128'
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
        :param listb: 输入时为空列表，用于存储虚拟子链接
    """
    soup = BeautifulSoup(html, 'html.parser')
    for div1 in soup.find_all(name='div', attrs={'class': "titleP"}):
        for aaa1 in div1.find_all('a'):
            lista.append(aaa1.attrs['title'])
            listb.append(aaa1.attrs['href'])


def get_child_html(url, listc):
    """
        根据指定的虚拟子网页的url，爬取虚拟子网页的html信息，并通过调用parse_script_url()，得到真实的子链接
        :param url: 基础链接 base_url2
        :param listc: 存储虚拟子链接的列表
    """
    for child in listc:
        child_url = url + child
        child_html = get_html_text(child_url, headers1, proxies1)
        parse_script_url(child_html, list3)


def parse_script_url(html, listd):
    """
        根据指定的虚拟子网页的html，提取得到真实的子链接
        :param html: 虚拟子网页的html文件
        :param listd: 输入时为空列表，用于存储真实的子链接
    """
    soup = BeautifulSoup(html, 'html.parser')
    script1 = soup.find(name='script', attrs={'type': "text/javascript"})
    string1 = script1.string
    result = re.search(r'"(http://.*?)";', string1)
    listd.append(result[1])


def parse_child_html(liste, listf):
    """
        根据指定真实子链接，爬取真实子网页的html信息，并调用write_to_file()进行存储
        :param liste: 存储真实子链接的列表
        :param listf: 存储标题信息的列表
    """
    t = -1
    for real_url in liste:
        real_html = get_html_text(real_url, headers1, proxies1)
        if real_html is None:
            continue
        else:
            t = t + 1
            soup = BeautifulSoup(real_html, 'html.parser')
            result1 = '----------标题' + str(t+1) + ': ' + listf[t] + '-----------------------------'
            save_to_file(result1)
            for div2 in soup.find_all(name='div', attrs={'class': "TRS_Editor"}):
                for ppp1 in div2.find_all('p'):
                    result2 = ppp1.string
                    save_to_file(result2)


def save_to_file(result):
    """
        将爬取的结果信息，存入本地的.txt文件中
        :param result: 爬取的结果信息
    """
    with open(file='Evs11.txt', mode='a', encoding='utf8') as f:
        f.write(str(result) + '\n')


def main(page):
    """
        主函数，用于爬取一页主网页中的子网页信息
        :param page: 网页的页数
    """

    start_url = base_url1 + goods + params + str(page)
    base_html = get_html_text(start_url, headers1, proxies1)
    parse_html_text(base_html, list1, list2)
    get_child_html(base_url2, list2)
    print(list3)
    parse_child_html(list3, list1)


if __name__ == '__main__':
    """
        用于启动主程序，遍历爬取n页主网页中的子网页信息   
    """
    for i in range(1, 11):
        list1 = []
        list2 = []
        list3 = []
        main(i)
        time.sleep(1)
