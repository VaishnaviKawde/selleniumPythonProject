import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
driver.get(url)

time.sleep(3)
# page scroll by pixel
driver.execute_script('window.scrollBy(0,3000)', "")

time.sleep(3)

# Scroll by or upto specific element
ele = driver.find_element(By.ID, 'Programming_examples')
driver.execute_script("arguments[0].scrollIntoView()", ele)

time.sleep(3)
#Scroll till the end of page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
time.sleep(3)

driver.execute_script("window.scrollTo(0,0)", "")
