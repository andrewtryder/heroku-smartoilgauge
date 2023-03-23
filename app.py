from selenium import webdriver
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

# setup our Chrome webdriver and go.
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# do we need this set window size?
browser.set_window_size(1440, 900)

# now do the actual login to smartoilgauge.
browser.get("https://app.smartoilgauge.com/app.php")
browser.find_element(By.ID,"inputUsername").send_keys(user_name)
browser.find_element(By.ID,"inputPassword").send_keys(password)
browser.find_element(By.CSS_SELECTOR,"button.btn").click()
browser.implicitly_wait(3)

# specifically find text with a '/' and split on that. 
nav = browser.find_element(By.XPATH, '//p[contains(text(), "/")]').text
nav_value = nav.split(r"/")

# quit the browser.
browser.quit()

# return and print the value.
print("{0}".format(nav_value[0]))