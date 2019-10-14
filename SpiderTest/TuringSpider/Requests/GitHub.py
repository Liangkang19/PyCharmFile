import requests

url = 'https://github.com/favicon.ico'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
r = requests.get(url=url, headers=headers)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
