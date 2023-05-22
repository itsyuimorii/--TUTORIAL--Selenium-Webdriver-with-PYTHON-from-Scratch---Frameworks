from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("/Users/itsyuimoriispace/Documents/GitHub/Selenium-Webdriver-with-PYTHON-from-Scratch---Frameworks/chromedriver_mac64/chromedriver");
driver = webdriver.Chrome(service = service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message