from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)
# element = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
# element.click()
# driver.switch_to.alert.accept()
#
# element2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
# element2.click()
# driver.switch_to.alert.dismiss()

element = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
element.click()
element2 = driver.switch_to.alert.accept()

