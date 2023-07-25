# from selenium import webdriver

# #chrome driver
# from selenium.webdriver.chrome.service import Service
# #-- Chrome
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

# #-- Firefox
# # service_obj = Service("/Users/rahulshetty/documents/geckodriver")
# # driver = webdriver.Firefox(service=service_obj)

# #-- Edge
# # service_obj = Service("/Users/rahulshetty/documents/msedgedriver")
# # driver = webdriver.Edge(service=service_obj)




# driver.maximize_window()
# driver.get("https://rahulshettyacademy.com")
# print(driver.title)
# print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.forward()
# driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

service_obj = Service("/opt/homebrew/bin/chromedriver")
# chrome driver will open the browser
driver = webdriver.Chrome(service=service_obj, options=options)

# maximize the browser
driver.maximize_window()

driver.get("https://rahulshettyacademy.com")
print(driver.title)
print("This is the current URL" + driver.current_url)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.minimize_window()
driver.back()
driver.refresh()
driver.close()



