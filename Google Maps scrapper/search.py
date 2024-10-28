from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
import time
import json

from school import search_place

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--no-sandbox")
#provide location where chrome stores profiles

options.add_argument(r"--user-data-dir=/home/ankit/.config/google-chrome")

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Default')

#provide the profile name with which we want to open browser
options.add_argument(r'--profile-directory=Profile 2')

#specify where your chrome driver present in your pc
search = input("Enter location name").replace(" ","+")+"/"
driver = webdriver.Chrome()
driver.get(search)


# .PLbyfe > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > a:nth-child(1)
# .PLbyfe > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > a:nth-child(1)
# SCROLL DOWN ENDLESS
while True:
    results = driver.find_elements(By.CLASS_NAME, 'THOPZb')
    driver.execute_script("return arguments[0].scrollIntoView();", results[-1])
    # time.sleep(1)
    try:
        # CONFIRM END OF THE PAGE  
        text = driver.find_element(By.CSS_SELECTOR,".HlvSq").text
        if text == "You've reached the end of the list.":
            break
    except:
        continue
        
# FINDING ELEMENT
elements = driver.find_elements(By.CSS_SELECTOR,".THOPZb a")
links = [e.get_attribute("href") for e in elements if e.get_attribute("href").__contains__("https://www.google.com/maps/place")]
# print(len(links))
# for i in range(len(links)):
#     print(links[i])
with open("link.json") as l:
    json.dumps(links,l)
driver.close()

# input("start")
# for l in links:
#     print(l)
#     search_place(l)
    


# input()

