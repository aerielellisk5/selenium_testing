# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# from selenium.webdriver.common.by import By
# name = "Rahul"
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# driver.find_element(By.ID, "alertbtn").click()
# alert = driver.switch_to.alert
# alertText = alert.text
# print(alertText)
# assert name in alertText
# alert.accept()
# #alert.dismiss()


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


name = "Aeriel"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
alert.accept()

assert name in alertText


# alert.accept will click on OK
# alert.dismiss() will click on Dismiss
