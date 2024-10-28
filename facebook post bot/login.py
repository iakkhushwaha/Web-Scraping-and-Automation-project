from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait

# Creating Instance
option = Options()

# Working with the 'add_argument' Method to modify Driver Default Notification
option.add_argument('--disable-notifications')

# Passing Driver path alongside with Driver modified Options
# browser = webdriver.Chrome(chrome_options= option)

# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 0}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver  = webdriver.Chrome(options= option)
# driver.set_permissions('notifications','--disable')
driver.get("https://www.facebook.com/")

email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME,"pass")
login = driver.find_element(By.NAME, "login")
# print(email, password)

email.send_keys("")
password.send_keys("")
login.click()

time.sleep(1)
write = driver.find_element(By.CSS_SELECTOR,".x1n2onr6")
print(write.text)
write.click()

