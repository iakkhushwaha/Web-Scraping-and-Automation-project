from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
import time
# import json


search = input("Enter location name").replace(" ","+")+"/"
driver = webdriver.Chrome()
driver.get(search)


# SCROLL DOWN ENDLESS
while True:
    results = driver.find_elements(By.CLASS_NAME, 'THOPZb')
    driver.execute_script("return arguments[0].scrollIntoView();", results[-1])
    # time.sleep(1)
    try:
        text = driver.find_element(By.CSS_SELECTOR,".HlvSq").text
        if text == "You've reached the end of the list.":
            break
    except:
        continue
        
# FINDING ELEMENT
elements = driver.find_elements(By.CSS_SELECTOR,".THOPZb a")
links = [e.get_attribute("href") for e in elements]
print(len(links))
print(links)

school_list = {}



