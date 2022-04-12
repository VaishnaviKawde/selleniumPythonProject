from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://seleniumbase.io/demo_page"
driver.get(url)
dropElement = driver.find_element(By.ID, "drop1")
print("Is dropElement is visible to user:", dropElement.is_displayed())

checkElement = driver.find_element(By.ID, "checkBox1")
print(" Is checkbox  is enabled for click: ", checkElement.is_enabled())
checkElement.click()
print("After checkbox click, is drop element visible to user: ", dropElement.is_displayed())
if dropElement.is_displayed():       # if(dropElement.is_displayed() == True)
    print("test case passed")
else:
    print("test case iss failed")

# driver.close()
