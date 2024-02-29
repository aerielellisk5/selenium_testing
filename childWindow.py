# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.service import Service

# service_obj = Service("/Users/rahulshetty/documents/geckodriver")
# driver = webdriver.Firefox(service=service_obj)
# driver.implicitly_wait(2)

# driver.get("https://the-internet.herokuapp.com/windows")
# driver.find_element(By.LINK_TEXT,"Click Here").click()
# windowsOpened = driver.window_handles

# driver.switch_to.window(windowsOpened[1])
# print(driver.find_element(By.TAG_NAME, "h3").text)
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()
# make sure the parent window has this text - Opening a new window

assert driver.find_element(By.CSS_SELECTOR, "h3").is_displayed()


windowsOpen = driver.window_handles
driver.switch_to.window(windowsOpen[1])
assert "New Window" == driver.find_element(By.CSS_SELECTOR, "h3").text
driver.close()
driver.switch_to.window(windowsOpen[0])
assert "Opening a new window" == driver.find_element(By.CSS_SELECTOR, "h3").text

