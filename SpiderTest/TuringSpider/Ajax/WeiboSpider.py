# Ajax: 异步的JavaScript和XML页面渲染
# http://www.w3school.com.cn/ajax/ajax_xmlhttprequest_send.asp
# http://m.weibo.cn/u/2830678474
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=3

import requests
from urllib.parse import urlencode
from pyquery import PyQuery
from pymongo import MongoClient

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
        'Host': 'm.weibo.cn',
        'Referer': 'https://m.weibo.cn/u/2830678474',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
}

client = MongoClient(host='127.0.0.1', port=27017)   # 连接本地数据库
db = client['weibo']                                 # 新建/指定数据库，名为'weibo'
collection = db['weibo_info']                        # 新建/指定数据库中的集合，名为‘weibo_info’
max_page = 10


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)      # 将params参数转化为URL的GET请求参数
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.json(), page

    except requests.ConnectionError as e:
        print('Error', e.args)
        return None


def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')      # 寻找data-->cards中的json数据
        for index, item in enumerate(items):       # enumerate()返回枚举对象
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')           # 寻找cards-->mblog中的json数据
                weibo = {
                    'id': item.get('id'),
                    'text': PyQuery(item.get('text')).text(),
                    'attitudes': item.get('attitudes_count'),
                    'comments': item.get('comments_count'),
                    'reposts': item.get('reposts_count')
                }
                yield weibo


def save_to_mongo(result):
    if collection.insert_one(result):    # 将数据插入到collection中
        print('Saved to Mongo')


if __name__ == '__main__':
    for page1 in range(1, max_page + 1):
        json1 = get_page(page1)
        results = parse_page(*json1)
        for result1 in results:
            print(result1)
            save_to_mongo(result1)
