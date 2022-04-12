import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://seleniumbase.io/demo_page"
driver.get(url)
element = driver.find_element(By.ID, "mySelect")
dropDown = Select(element)
# create dropdown object with class Select # Select is accepting argument to create dropdown object
dropDown.select_by_index(2)
time.sleep(5)
dropDown.select_by_value('25%')
time.sleep(5)
dropDown.select_by_visible_text("Set to 100%")

