# Chrome 代理测试

from selenium import webdriver

proxy = '181.118.155.29:41021'
url = 'http://httpbin.org/get'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=https://' + proxy)
browser = webdriver.Chrome(options=chrome_options)
browser.get(url=url)
