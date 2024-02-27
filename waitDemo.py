# import time

# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# from selenium.webdriver.common.by import By

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(5)
# # 5 seconds is max time out.. 2 seconds (3 seconds save)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
# time.sleep(2)
# results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#list[]
# count = len(results)
# assert count > 0
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()

# driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
# driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# print(driver.find_element(By.CLASS_NAME,"promoInfo").text)

















from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.implicitly_wait(5)
# driver will wait max 5 seconds to wait for an element to appear on the page
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
# print(len(results))
# assert count > 3

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("rahulshettyacademy")
# getting an error that element is not interactable?
# time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

confirmation = driver.find_element(By.CLASS_NAME, "promoInfo")
assert confirmation.is_displayed()


    