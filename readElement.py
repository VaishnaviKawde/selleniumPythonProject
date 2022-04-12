
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("")
driver = webdriver.Chrome(service=s)
url = "https://seleniumbase.io/demo_page"
driver.get(url)

inputElement = driver.find_element(By.ID, "myTextInput2")
inputText = inputElement.get_attribute("value")  # Read value/text from value attribute
print("Input Text : ", inputText)

inputElement.clear()
inputElement.send_keys("new text")

print("Input Text : ", driver.find_element(By.ID, "myTextInput2").get_attribute("value"))

print("Input field name : ", driver.find_element(By.ID, "myTextInput2").get_attribute("name"))

