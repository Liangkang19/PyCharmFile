# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190901&ie=utf8&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0
# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190901&ie=utf8&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44
# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20190901&ie=utf8&bcoffset=0&ntoffset=6&p4ppushleft=1%2C48&s=88
# https://curl.trillworks.com/ids=222887%2C222890%2C222889%2C222886%2C222906%2C222898%2C222907%2C222885%2C222895%2C222878%2C222908%2C222879%2C222893%2C222896%2C222918%2C222917%2C222888%2C222902%2C222880%2C222913%2C222910%2C222882%2C222883%2C222921%2C222899%2C222905%2C222881%2C222911%2C222894%2C222920%2C222914%2C222877%2C222919%2C222915%2C222922%2C222884%2C222912%2C222892%2C222900%2C222923%2C222909%2C222897%2C222891%2C222903%2C222901%2C222904%2C222916%2C222924
# callback=tbh_service_cat

import re
import requests


def getHTMLText(url, headers):
    try:
        r = requests.get(url=url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('爬取成功！')
        return r.text
    except:
        print('爬取失败！')
        return ''


def parsePage(ilt, html):
    try:
        plt = re.findall(r'"view_price":"(.*?)"', html)
        tlt = re.findall(r'"raw_title":"(.*?)"', html)
        for i in range(plt):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append(price, title)
    except:
        print('')


def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))

    print('')


def taobaomain():
    goods = '手机'
    deepth = 2
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Cookie': 'thw=cn; t=3cde6061953ab6b6269b6126a112ff19; enc=rX8OeAZ0tXc1xEU6IDoknq6U3rFWm6u46V%2FO%2Bxh4s2xYIEaLDBsBW1nCJUVLIvtFRvkhufMREvDFLA%2FJS3%2BFyg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156;\
         x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0;\
         cookie2=15da87964e8dedbe828ed39aa1e5c67f; _tb_token_=e333b9b17339b; cna=2fjzFbWqo1ECAXWIGFQpxL+b;\
         v=0; unb=2656216698; uc3=vt3=F8dByuKzhuK95ylTKCU%3D&lg2=W5iHLLyFOGW7aA%3D%3D&nk2=pMZo%2FCs79udur1fYFw5k&id2=UU6kVW%2Fs2qVYFQ%3D%3D; csg=595890fe; lgc=%5Cu5343%5Cu53EA%5Cu9E64573070168;\
          cookie17=UU6kVW%2Fs2qVYFQ%3D%3D; dnk=%5Cu5343%5Cu53EA%5Cu9E64573070168; skt=1d93aa9685359a37; existShop=MTU2ODUxODIxOA%3D%3D; uc4=id4=0%40U2xpV1kWlYiVao8BmUqxCbZHVluU&nk4=0%40pgXvqFpvOD9I4UuGfONN4cgBymazhAzZCP8%3D;\
          tracknick=%5Cu5343%5Cu53EA%5Cu9E64573070168; _cc_=VFC%2FuZ9ajQ%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=88d; _nk_=%5Cu5343%5Cu53EA%5Cu9E64573070168;\
          cookie1=BxeC3FXGvpCilquTlrCLvjw%2FJoeeL7zMfSk6HH%2BWPY4%3D; mt=ci=5_1;\
          uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=V32FPkk%2FgihF%2FS5nr3O5&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTaECPUXzOjeQ%3D%3D&tag=8&lng=zh_CN;\
          isg=BP7-DQpxL9Q0JnvjnZskx2ZfTxRAP8K5d2czEagHX8E8S54lEM8SySQhxxeH87rR; l=cBSl-qBIqykdRkA9BOCwourza77OSIRAguPzaNbMi_5CY6L1_xbOkyOBBFp6VjWd9zLB4JuaUM29-etkiTZNApDgcGAN.'
    }
    start_url = 'https://s.taobao.com/search?q=' + goods
    infolist = []
    for i in range(deepth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url=url, headers=headers)
            parsePage(infolist, html)
        except:
            continue
    printGoodsList(infolist)


taobaomain()
