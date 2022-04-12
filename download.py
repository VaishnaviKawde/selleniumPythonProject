import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/download"
driver.get(url)
time.sleep(3)

driver.find_element(By.LINK_TEXT, 'screenshot.png').click()
driver.close()