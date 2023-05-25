import pytest
from selenium import webdriver
import time
driver = None



@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\ymorii\\Desktop\\work_folder\\github\\Selenium-Webdriver-with-PYTHON-from-Scratch---Frameworks\\chromedriver_mac64\\chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\ymorii\\Desktop\\work_folder\\github\\Selenium-Webdriver-with-PYTHON-from-Scratch---Frameworks\\chromedriver_mac64\\chromedriver")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver= driver
    yield
    driver.close()