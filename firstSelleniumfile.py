from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//selfg//chromedriver.exe")
driver.get("https://www.facebook.com/")
print("Page Title : ", driver.title)
print("Page Current Url : ", driver.current_url)
driver.back()             # back button on browser
driver.forward()       # forward button on browser
driver.close()      # close current window
driver.quit()          # Quits the driver and closes every associated window.
