from selenium import webdriver
from selenium.webdriver.chrome.service import Service


#Create the Chrome service object, which send as a property of the chrome class.
servie_obj = Service("");

#Provided us with proxy drivers, call the actual browser.
webdriver.Chrome(service = servie_obj)

