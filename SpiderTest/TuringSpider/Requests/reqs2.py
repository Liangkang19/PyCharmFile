import requests

url = 'http://httpbin.org/post'
dict1 = {'name': 'laosi', 'address': 'hainan'}
files = {'files': open('favicon.ico', 'rb')}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
r = requests.post(url=url, data=dict1, files=files, headers=headers)
print(r.text)
