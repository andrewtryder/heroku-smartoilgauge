from selenium import webdriver
from pyvirtualdisplay import Display
from webdriver_manager.chrome import ChromeDriverManager
import os

user_name = os.environ['SMARTOIL_USERNAME']
password = os.environ['SMARTOIL_PASSWORD']

display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(ChromeDriverManager().install(),options=options)
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

display.stop()
