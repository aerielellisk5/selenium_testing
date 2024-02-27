# import time

# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# #['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(2)
# # 5 seconds is max time out.. 2 seconds (3 seconds save)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
# time.sleep(4)

# results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#list[]
# count = len(results)
# assert count > 0
# for result in results:
#     result.find_element(By.XPATH,"div/button").click()

# driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()  #15
# driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

# #Sum validation
# prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
# sum = 0
# for price in prices:
#    sum = sum + int(price.text)

# print(sum)
# totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

# assert sum == totalAmount






# driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# print(driver.find_element(By.CLASS_NAME,"promoInfo").text)






from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5) #max timeout


driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results_of_products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results_of_products)
assert count > 0

# chaining method in selenium
for result in results_of_products:
    result.find_element(By.XPATH, "div/button").click()

# Create a list of expected list of the prodcut text

groceryList = []
    
for itemName in results_of_products:
    item = itemName.find_element(By.XPATH, "h4").text
    # print(item)
    groceryList.append(item)
    print(groceryList)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

# WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# print(driver.find_element(By.CLASS_NAME, "promoInfo").text)




### Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(total)
sum = 0


for price in prices:
    sum = sum + int(price.text)
    # print(sum)
    # print(total)

assert sum == total

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discountAmt")))

#  Need to write code to test that Total Amount is always more than total after discount

time.sleep(10)
discountedTotal = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(discountedTotal)

assert total > discountedTotal






