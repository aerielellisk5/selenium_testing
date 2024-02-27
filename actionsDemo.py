# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# action = ActionChains(driver)
# #action.double_click(driver.find_element(By.))
# #action.context_click()
# #action.drag_and_drop()
# action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# #action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
# action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

action = ActionChains(driver)
# action.double_click(driver.find_element(By.))
# action.context_click() aka Right Click
# action.drag_and_drop()
# action.move_to_element()

# to scroll the selected element into view
driver.execute_script("document.getElementById('mousehover').scrollIntoView()")

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()


