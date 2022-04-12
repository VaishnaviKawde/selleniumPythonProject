from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = "https://the-internet.herokuapp.com/windows"
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()
print("currently active handle/window ", driver.current_window_handle)
handles = driver.window_handles
print("all handles", handles)
# driver.switch_to.window(handles[1])
# textElement = driver.find_element(By.XPATH, '/html/body/div/h3')
# print(textElement.text)

for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == 'Dashboard':
        break
