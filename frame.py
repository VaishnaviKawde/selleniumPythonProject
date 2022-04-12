import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert"
driver.get(url)
driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH, 'html/body/button').click()
time.sleep(3)
driver.switch_to.alert.accept()
