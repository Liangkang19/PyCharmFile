import requests
from bs4 import BeautifulSoup

url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup1 = BeautifulSoup(demo, 'html.parser')
for link in soup1.find_all('a'):
    print(link.get('href'))

print(soup1.find_all(['a', 'b']))

