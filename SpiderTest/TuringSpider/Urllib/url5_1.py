# 登录信息: Cookies的处理

from http.cookiejar import CookieJar
from http.cookiejar import LWPCookieJar
from http.cookiejar import MozillaCookieJar
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor


file_name = 'cookies1.txt'
# cookie = CookieJar()                     # 声明CookieJar对象
# cookie = LWPCookieJar(file_name)         # 声明LWPCookieJar对象
cookie = MozillaCookieJar(file_name)       # 声明MozillaCookieJar对象

handler = HTTPCookieProcessor(cookie)      # 建立Handler
opener = build_opener(handler)             # 建立Opener
res = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + ' = ' + item.value)
cookie.save(ignore_discard=True, ignore_expires=True)  # cookie信息写入txt中
