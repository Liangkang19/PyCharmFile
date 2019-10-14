# 验证：opener
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from urllib.request import HTTPBasicAuthHandler
from urllib.request import build_opener
from urllib.error import URLError

username = 'username'
password = 'password'
url = 'http://localhost:5000/'
p1 = HTTPPasswordMgrWithDefaultRealm()          # 构造登录对象
p1.add_password(None, url, username, password)  # 添加登录信息
auth_handle = HTTPBasicAuthHandler(p1)          # 用于管理认证
opener = build_opener(auth_handle)              # 建立处理验证的处理器
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
