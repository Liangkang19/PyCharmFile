# 获取cookies
import requests

url = 'https://www.zhihu.com'
headers = {
    'Cookie': '_zap=10fdd2a5-1203-4b43-b7ef-a1443ac89e27;\
     d_c0="AMDiJQU8BhCPTqGGIoq5CkdJiaX6R3y5qeU=|1568076294";\
     _xsrf=HdlYDQAIEFI1ivntfxdFLxcOi4oXRa5I;\
     tgw_l7_route=4860b599c6644634a0abcd4d10d37251;\
     capsion_ticket="2|1:0|10:1568515725|14:capsion_ticket|44:ODg4YmRmNjU4MGZhNDE4NmJlMGVkOWMxYzRlNTQ4MmY=|06c33f9d7b2fd01f9dfa105b940174fbb17c13bf35a23cd35dff37c12b0fba6e";\
     z_c0="2|1:0|10:1568515763|4:z_c0|92:Mi4xZzZmS0JBQUFBQUFBd09JbEJUd0dFQ2NBQUFDRUFsVk5zek9sWFFBOFJqWHRva1paWGJFYlZobDE2dkk3VmVKcV9B|9fbbe2ba248f48833e89e4ae25ef778a9893c4937481cd186901fd3bc99beed0";\
     tst=r',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}
r = requests.get(url=url, headers=headers)
print(r.cookies)
