# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")
# chrome_options.add_argument("--ignore-certificate-errors")

# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj, options=chrome_options)
# driver.implicitly_wait(2)

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# driver.get_screenshot_as_file("screen.png")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()

# headmode vs headless mode --> headless will make sure that it won't open up the browser
options.add_argument("headless")
option.add_argument("--ignore-certificate-errors")


options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
service_obj = Service("/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# scroll to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# take a screenshot
driver.get_screenshot_as_file("screen4.png")

