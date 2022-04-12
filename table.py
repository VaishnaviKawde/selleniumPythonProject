import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://www.w3schools.com/html/html_tables.asp"
driver.get(url)

rows = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr'))
columns = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th'))
print("no. of rows", rows)
print("no .of columns", columns)

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').text, end="   ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[2]').text, end="   ")
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[3]').text)
for element in range(rows+2):
    for ele in range(columns+1):
        value = driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr["+str(element)+"]/td["+str(ele)+"]').text
        print(value, end="  ")
    print()
