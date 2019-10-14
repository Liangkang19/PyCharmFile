# 切换父子页面：Frame
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)
driver.switch_to.frame('iframeResult')
try:
    logo = driver.find_element(By.CSS_SELECTOR, '.logo')
except NoSuchElementException:
    print('No logo')
driver.switch_to.parent_frame()
logo = driver.find_element(By.CSS_SELECTOR, '.logo')
print(logo)
print(logo.text)
