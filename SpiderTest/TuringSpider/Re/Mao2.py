import requests
import time
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_one_page(url, headers):                   # 爬取函数
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('爬取成功！')
        return r.text

    except RequestException:
        print('爬取失败！')
        return None


def parse_one_page(html, list1, list2, list3):
    soup = BeautifulSoup(html, 'html.parser')
    for div1 in soup.find_all(name='div', attrs={'class': "movie-item-info"}):
        pps = div1.find_all('p')
        list1.append([pps[0].string, pps[2].string[5:15]])

    for p1 in soup.find_all(name='p', attrs={'class': "score"}):
        iis = p1.find_all('i')
        list2.append(iis[0].string + iis[1].string)

    for dd in soup.find_all(name='dd'):
        iis = dd.find('i')
        list3.append(iis.string)


def write_to_file(list1, list2, list3):
    for i in range(len(list1)):
        u1 = list1[i]
        result1 = [list3[i], u1[0], u1[1], list2[i]]
        with open(file='result.txt', mode='a', encoding='utf8') as f:
            f.write(str(result1) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)  # 共提取10个网页内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    html = get_one_page(url, headers)  # 每个网页对应的信息代码
    list1 = []
    list2 = []
    list3 = []
    parse_one_page(html, list1, list2, list3)
    write_to_file(list1, list2, list3)


if __name__ == '__main__':
    for t in range(10):
        main(offset=t*10)
        time.sleep(2)

# print('{:^10}\t{:^7}\t{:^8}\t{:^10}\t'.format('电影名称', '上映时间', '评分', '排名'))
#     for i in range(len(list1)):
#         u1 = list1[i]
#         print('{:^10}\t{:^10}\t{:^10}\t{:^10}\t'.format(u1[0], u1[1], list2[i], list3[i]))
# def write_to_file(result):       # 把提取出来的信息写到文件夹
