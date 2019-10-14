# 获取属性节点

import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

chrome_op = ChromeOptions()
chrome_op.add_argument('--headless')
driver = Chrome(options=chrome_op)             # 启动无界面模式
url = 'http://www.zhihu.com/explore'
driver.get(url)
WebDriverWait(driver, 10)
Button = driver.find_element(By.CSS_SELECTOR, '[class="ExploreSpecialCard-contentTag"]')
print(Button.text)
