# 网页的前进和后退,转换页面

import time
from selenium.webdriver import Chrome
driver = Chrome()
driver.get('http://www.baidu.com')
time.sleep(2)
driver.execute_script('window.open()')
driver.switch_to.window(driver.window_handles[1])
driver.get('http://www.taobao.com')
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
driver.get('http://www.qq.com')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
