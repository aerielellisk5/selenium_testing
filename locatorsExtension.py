from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

service_obj = Service("/opt/homebrew/bin/chromedriver")
# chrome driver will open the browser
driver = webdriver.Chrome(service=service_obj, options=options)

# Regular Selectors
driver.get("https://rahulshettyacademy.com/client")
# driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
# driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
# #driver.find_element(By.XPATH,"//button[@type='submit']").click()
# driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
# for XPATH selectors
driver.find_element(By.XPATH, "//form/div[2]/input").click()

# for CSS selectors
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("helloo")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("helloo")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()







# driver.close()