# 猫眼电影爬取通过正则表达式
import re
import json
import time
import requests
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


def parse_one_page(html):         # 提取出，‘序列号’，‘电影标题’，‘上映时间’，‘评分’
    pattern = re.compile(r'<dd>.*?board-index.*?>(\d+)</i>.*?<a.*?title="(.*?)".*?'
                         + r'<p.*?releasetime">(.*?)</p>.*?<i.*?integer">(.*?)</i>'
                         + r'.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # 使用compile编译正则表达式
    items = re.findall(pattern, html)          # 将html中的信息与pattern对比
    for item in items:
        yield{
            'index': item[0],
            'title': item[1],
            'releasetime': item[2].strip()[5:],  # str.strip()就是把这个字符串头和尾的空格，以及位于头尾的\n \t之类给删掉
            'score': item[3]+item[4]
        }
# yield 相当于高级的 return，
# 1.解析程序第一次执行，for循环中的第一组yield中的数据返回一次，解析程序在yield处中断
# 2.解析程序第二次执行，for循环中的第二组yield中的数据返回一次，解析程序在yield处中断
# 3.解析晨曦第n次执行，for循环中断，解析程序不再执行


def write_to_file(content):       # 把提取出来的信息写到文件夹
    # mode='a' : 以写入模式打开，若文件已存在，数据在添加至末尾
    with open(file='result.txt', mode='a', encoding='utf8') as f:
        f.write(json.dumps(obj=content, ensure_ascii=False)+'\n')
        f.close()
# json.dumps()用于将字典形式的数据转化为字符串
# json.loads()用于将字符串形式的数据转化为字典
# ensure_ascii=False：是数据中的中文字符能正确输出


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)  # 共提取10个网页内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    html = get_one_page(url, headers)     # 每个网页对应的信息代码
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
