from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://seleniumbase.io/demo_page"
driver.get(url)
elements = driver.find_elements(By.TAG_NAME, "a")
for element in elements:
    print(element.text)

# element = driver.find_element(By.LINK_TEXT, "SeleniumBase on GitHub").click()
# driver.back()
#driver.forward()
element = driver.find_element(By.PARTIAL_LINK_TEXT, "salenium")
