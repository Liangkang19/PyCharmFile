# IP地址归属地的自动查询
import requests

url = 'http://m.ip138.com/ip.asp?ip='
IP = '55.55.55.55'
try:
    r = requests.get(url+IP)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
    print('爬取成功！')
except:
    print('爬取失败！')


# url = 'http://m.ip138.com/ip.asp?ip='
# IP = '202.204.80.112'
# IP = '55.55.55.55'
# r = requests.get(url+IP)
# print(r.status_code)
# print(r.text[-500:])

