
from datetime import time
from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/itsyuimoriispace/Documents/GitHub/Selenium-Webdriver-with-PYTHON-from-Scratch---Frameworks/chromedriver_mac64/chromedriver");
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, 'autosuggest')
time.sleep(2)