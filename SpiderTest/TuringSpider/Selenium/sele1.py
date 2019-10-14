# 模拟浏览器:Chrome
# API:Application Programming Interface(应用程序编程接口)


import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

driver = Chrome()                              # 设置浏览器为Chrome浏览器
driver.maximize_window()                       # 最大化浏览器窗口
try:
    driver.get('http://www.baidu.com')         # 输入网址并打开
    input1 = driver.find_element(By.ID, 'kw')  # 定位搜索框，设置元素属性为：keywords
    input1.send_keys('Python')                 # 在搜索框输入关键词：Python
    input1.send_keys(Keys.ENTER)               # 模拟键入关键词：按下Enter键
    wait = WebDriverWait(driver, 10)           # 等待网页加载，10s内未响应，抛出错误：TimeoutException
    wait.until(ec.presence_of_all_elements_located((By.ID, 'content_left')))
    # 等待，直到找到目前存在的所有元素
    print(driver.current_url)                      # 输出网页的URL
    print(driver.get_cookies())                    # 输出网页的cookies
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 设置滚动距离：从0到网页底部
    driver.execute_script('alert("To Bottom")')    # 将进度条下拉到底
    # print(driver.page_source)                    # 输出网页的源代码
finally:
    time.sleep(5)
    driver.close()
