import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/upload"
driver.get(url)

# time.sleep(3)
#
driver.find_element(By.ID, 'file-upload').send_keys("C:\\Users\\selfg\\Documents\\Zoom\\zoom.jpg")
#
driver.find_element(By.ID, 'file-submit').click()

