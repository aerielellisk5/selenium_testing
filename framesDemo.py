# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service

# service_obj = Service("/Users/rahulshetty/documents/geckodriver")
# driver = webdriver.Firefox(service=service_obj)
# driver.implicitly_wait(2)

# driver.get("https://the-internet.herokuapp.com/iframe")
# driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.ID,"tinymce").clear()
# driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
# driver.switch_to.default_content()
# print(driver.find_element(By.CSS_SELECTOR,"h3").text)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)










