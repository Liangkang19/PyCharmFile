# 模拟Chrome查找网页中的多节点参数

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()                              # 设置浏览器为Chrome浏览器
driver.get('http://www.taobao.com')
list1 = driver.find_elements(By.CSS_SELECTOR, '.service-bd li a')  # 使用CSS选择器的相关知识
print(list1)
time.sleep(5)
driver.close()
