# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# driver.find_element(By.ID, "autosuggest").send_keys("ind")
# time.sleep(2)
# countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
# print(len(countries))

# for country in countries:
#     if country.text == "India":
#         country.click()
#         break
# #print(driver.find_element(By.ID, "autosuggest").text)

# assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


driver.find_element(By.ID, "autosuggest").send_keys("ind")
print("start of the driver")
time.sleep(5)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# print(driver.find_element(By.ID, "autosuggest").text) --> this wont load the country name because it grabs the text on the page once the application is initially loaded

print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))



# driver.close()








