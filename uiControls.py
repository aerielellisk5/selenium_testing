# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# from selenium.webdriver.common.by import By

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

# print(len(checkboxes))

# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option2":
#         checkbox.click()
#         assert checkbox.is_selected()
#         break

# radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
# radiobuttons[2].click()
# assert radiobuttons[2].is_selected()

# assert driver.find_element(By.ID,"displayed-text").is_displayed()
# driver.find_element(By.ID,"hide-textbox").click()
# assert not driver.find_element(By.ID,"displayed-text").is_displayed()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# print(len(checkboxes))

# for checkbox in checkboxes:
#     # print(checkbox)
#     if checkbox.get_attribute("value") == "option2":
#         # checkbox.click()
#         assert checkbox.is_selected()
#         break
    
radioButtons = driver.find_elements(By.XPATH, "//input[@type='radio']")

for radioButton in radioButtons:
    if radioButton.get_attribute("value") == "radio2":
        radioButton.click()
        assert radioButton.is_selected()


# show/hide example
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()





# driver.close()