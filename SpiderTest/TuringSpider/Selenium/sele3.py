# 模拟动作链

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
driver.get(url)
driver.switch_to.frame('iframeResult')
source = driver.find_element(By.CSS_SELECTOR, '#draggable')  # 拖拽块的源位置
target = driver.find_element(By.CSS_SELECTOR, '#droppable')  # 拖拽块的目标位置
actions = ActionChains(driver)                               # 设置动作链
actions.drag_and_drop(source, target)                        # 设置源和目标的连接
actions.perform()                                            # 移动块
try:
    logo = driver.find_element(By.CSS_SELECTOR, '.logo')
except NoSuchElementException:
    print('No logo')
driver.switch_to.parent_frame()
logo = driver.find_element(By.CSS_SELECTOR, '.logo')
print(logo)
print(logo.text)
