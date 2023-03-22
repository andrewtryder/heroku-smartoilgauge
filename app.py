from selenium import webdriver
from pyvirtualdisplay import Display
import os

user_name = os.environ['SMARTOIL_USERNAME']
password = os.environ['SMARTOIL_PASSWORD']

#display = Display(visible=0, size=(800, 600))
#display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

browser.set_window_size(1440, 900)

browser.get("https://app.smartoilgauge.com/app.php")
browser.find_element_by_id("inputUsername").send_keys(user_name)
browser.find_element_by_id("inputPassword").send_keys(password)
browser.find_element_by_css_selector("button.btn").click()
browser.implicitly_wait(3)

nav = browser.find_element_by_xpath('//p[contains(text(), "/")]').text
nav_value = nav.split(r"/")
browser.quit()
print("{0}".format(nav_value[0]))

#display.stop()
