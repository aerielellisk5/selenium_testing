from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/documents-request")
driver.implicitly_wait(10)

# grab the email address; slice/trim, for just email
sentence = driver.find_element(By.CSS_SELECTOR, ".red").text
# print(sentence)
splitSentence = sentence.split()
email = splitSentence[4]
# print(email)
driver.get("https://rahulshettyacademy.com/loginpagePractise")

# go to next page and use the email and type a random password to retreive the error msg
driver.find_element(By.ID, "username").send_keys(email)

driver.find_element(By.ID, "password").send_keys("incorrect")

driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert")))

assert driver.find_element(By.CSS_SELECTOR, ".alert")
print("successful!")