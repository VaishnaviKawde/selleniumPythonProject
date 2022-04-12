from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logging.basicConfig(filename="CT8.log", format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — '
                                               '%(message)s', filemode='w')
logger = logging.getLogger('logger_Name')

logger.setLevel(logging.DEBUG)
try:

    logger.info('LoggingForFacebook.py script execution has been started...')
    logger.info('initializing web driver for chrome')
    s = Service("C://Users//selfg//chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    logger.info('initialized web driver for chrome')
    logger.debug('opening webpage or url : https://www.facebook.com/')
    url = 'https://www.facebook.com'
    driver.get(url)
    logger.debug('opening webpage or url : https://www.facebook.com/')

    logger.info("finding email element")
    inputEmail = driver.find_element(By.ID, "emaidl")
    inputEmail.send_keys("sdfadf@gmail.com")

    inputPass = driver.find_element(By.ID, "pass")
    inputPass.send_keys("password@123")

    btnLogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

    btnLogin.click()
    logger.info(" tst case passed")

except Exception as e:
    logger.error(f"Error occurred in facebook test: {e}")
