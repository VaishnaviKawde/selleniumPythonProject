
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/dynamic_loading/2"
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="start"]/button').click()
# time.sleep(10)       #  python - script will stop execution for 10 sec

# #it will be applicable for all controls
driver.implicitly_wait(60)     # selenium- it will pause/wait for maximun 120 to appear element on page and minimum 0 sec
eleH4 = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(eleH4.text)