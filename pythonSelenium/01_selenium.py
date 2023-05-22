from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Create the Chrome service object, which send as a property of the chrome class.
servie_obj = Service("/Users/itsyuimoriispace/Documents/GitHub/Selenium-Webdriver-with-PYTHON-from-Scratch---Frameworks/chromedriver_mac64/chromedriver");

#Provided us with proxy drivers, call the actual browser.
driver = webdriver.Chrome(service = servie_obj)

driver.get("https://www.google.com")
print(driver.title)
driver.close()
