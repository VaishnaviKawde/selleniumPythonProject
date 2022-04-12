import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
driver.get(url)
time.sleep(3)

drop1 = driver.find_element(By.ID, 'box3')
drop2 = driver.find_element(By.ID, 'box103')
time.sleep(3)
action = ActionChains(driver)
action.drag_and_drop(drop1, drop2).perform()
