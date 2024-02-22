# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# driver.get("https://rahulshettyacademy.com/angularpractice/")

# # ID, Xpath, CSSSelector, Classname, name, linkText
# driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
# driver.find_element(By.ID, "exampleCheck1").click()

# # Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# # CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname
# driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
# driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# #Static Dropdown
# dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
# dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(0)
# #dropdown.select_by_value()


# driver.find_element(By.XPATH, "//input[@type='submit']").click()
# message = driver.find_element(By.CLASS_NAME, "alert-success").text
# print(message)
# assert "Success" in message

# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
# driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

service_obj = Service("/opt/homebrew/bin/chromedriver")
# chrome driver will open the browser
driver = webdriver.Chrome(service=service_obj, options=options)

# Regular Selectors


driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, 'exampleInputPassword1').send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH Selectors
# //tagname[@attribute='value'] --> //input[@type='submit']



#Xpath - //tagname[@attribute='value']
#CSS - tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Aeriel")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hellowworld")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()




# CSS Selectors
# tagname[attribute='value']
#  #id
#  .class-name




# working with static dropdowns

# dropdown.select_by_index(0) --> male

# dropdown.select_by_value()
















driver.close()












