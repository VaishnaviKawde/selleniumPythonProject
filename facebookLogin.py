 #For latest version
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = 'https://www.facebook.com'
driver.get(url)


inputEmail = driver.find_element(By.ID, "email")
inputEmail.send_keys("sdfadf@gmail.com")

inputPass = driver.find_element(By.ID, "pass")
inputPass.send_keys("password@123")

btnLogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

btnLogin.click()
# driver.close()