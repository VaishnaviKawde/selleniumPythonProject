import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/dynamic_loading/2"
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

eleH4 = WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4') ))

#eleH4 = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(eleH4.get_attribute("innerHTML"))