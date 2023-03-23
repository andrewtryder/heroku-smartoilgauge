from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pybrake
import os

# setup Airbrake
notifier = pybrake.Notifier(project_id=488883,
                            project_key='2941cd71132a2e87e162200ae71fac82',
                            environment='production')

# our variables for smart oil gauge.
user_name = os.environ['SMARTOIL_USERNAME']
password = os.environ['SMARTOIL_PASSWORD']

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('disable-dev-shm-usage') # added in order to avoid the error session deleted because of page crash
options.add_argument('no-sandbox')
options.add_argument("window-size=1920,1080")  # need this for the code to work. Some sites don't render properly with headless.

# service = Service(r"C:\chromedriver.exe")
try:
    service = Service(os.environ['CHROMEDRIVER_PATH'])
    browser = webdriver.Chrome(service=service, options=options)
except Exception as err:
    notifier.notify("ERROR starting chrome: {0}".format(err))

# now do the actual login to smartoilgauge.
smartoilgaugeUrl = "https://app.smartoilgauge.com/app.php"
browser.get(smartoilgaugeUrl)
browser.find_element(By.ID,"inputUsername").send_keys(user_name)
browser.find_element(By.ID,"inputPassword").send_keys(password)
browser.find_element(By.CSS_SELECTOR,"button.btn").click()
browser.implicitly_wait(3)

# specifically find text with a '/' and split on that. 
nav = browser.find_element(By.XPATH, '//p[contains(text(), "/")]').text
print(nav)
nav_value = nav.split(r"/")

# quit the browser.
browser.quit()

# return and print the value.
print("{0}".format(nav_value[0]))