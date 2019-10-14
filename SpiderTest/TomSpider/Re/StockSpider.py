# http://quote.eastmoney.com/stock_list.html 东方财富网
# https://gupiao.baidu.com/stock/    百度股票
# if __name__=='__main__'
# 类似于别的编程语言的主函数,意思是如果这个python脚本是直接执行的,
# 则if__name__=='__main__'下面的代码就会被执行,
# 如果这个python脚本是被import到其他脚本中,则这段代码不会被执行
# html+css+js

import requests
from bs4 import BeautifulSoup
import traceback
import re



def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text[:1000])
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    # print(stockURL)
    a = soup.find_all('a')
    # print(a[0:1000])
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue
    return lst


def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        # print(html)

        try:
            if html == "":
                continue
            infoDick = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDick.update({'股票名称': name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                # print(val)
                infoDick[key] = val

                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write(str(infoDick)+'\n')
                    # print(i)
        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = 'http://quote.eastmoney.com/stock_list.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduDownload/stockinfo.txt'
    slist = []
    slist = getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


main()
