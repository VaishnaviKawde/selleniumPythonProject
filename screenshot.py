from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service("C://Users//selfg//chromedriver.exe")
driver = webdriver.Chrome(service=s)
url = 'https://www.facebook.com'
driver.get(url)

driver.get_screenshot_as_file('C:\\Python\\screenshotFacebook2.jpg')
driver.save_screenshot('screenshotFacebook.png')
