from pymongo import MongoClient
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery
from urllib.parse import quote
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(browser, 10)
client = MongoClient(host='127.0.0.1', port=27017)
db = client['Taobao']
collection = db['taobao_info'] 
MAX_PAGE = 100
KEYWORD = 'ipad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input1 = wait.until(
                ec.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input1')))
            submit = wait.until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input1.clear()
            input1.send_keys(page)
            submit.click()
        wait.until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    html = browser.page_source
    doc = PyQuery(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    """
    try:
        if collection.insert_one(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
        time.sleep(2)
    browser.close()


if __name__ == '__main__':
    main()

