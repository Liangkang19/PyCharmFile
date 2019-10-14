# 登录信息: 本地Cookies的上传

from http.cookiejar import LWPCookieJar
from urllib.request import build_opener
from urllib.request import HTTPCookieProcessor

cookie = LWPCookieJar()
# 上传本地cookie文件
cookie.load('cookies2.txt', ignore_discard=True, ignore_expires=True)
handler = HTTPCookieProcessor(cookie)      # 建立Handler
opener = build_opener(handler)             # 建立Opener
res = opener.open('http://www.baidu.com')
text = res.read().decode('utf-8')
print(text)
