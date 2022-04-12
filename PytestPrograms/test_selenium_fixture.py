import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def setup():
    global driver
    s = Service("C://Users//selfg//chromedriver//chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield
    print(driver.title)
    print(driver.close())


def test_1(setup):
    url = 'https://www.facebook.com'



def test_2(setup):
    url = 'https://www.gmail.com'
    driver.get(url)
    print(" gmail")


def test_3(setup):
    url = 'https://www.amazon.com'
    driver.get(url)
    print("amazon")