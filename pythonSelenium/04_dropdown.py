
from datetime import time
from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver
 #-- Chrome
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def main():
    service = Service('/Users/itsyuimoriispace/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(service=service)

    driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

    driver.find_element(By.ID, 'autosuggest').send_keys('ca')
    time.sleep(2)
    countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
    print(len(countries))

    for country in countries:
        if country.text == "Canada":
            country.click()
            break
    #print(driver.find_element(By.ID, "autosuggest").text)

    # assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "canada"




if __name__ == '__main__':
    main()
