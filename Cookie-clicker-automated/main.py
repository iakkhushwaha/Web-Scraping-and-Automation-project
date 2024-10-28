from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
print("buhf")
driver.get("http://orteil.dashnet.org/experiments/cookie/")
timeout = 5
game_timeout =  time.time()

# taking best decision
def best_decison():
    time.sleep(0.1)
# BUTTONS
    # money = driver.find_element(By.ID,"money")
    # grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
    # factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
    # mine = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
    # shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
    # alchemy_lab = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab b")
    # portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
    # time_machine = driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine b")


    # VARIABLES
    MONEY = int(driver.find_element(By.ID,"money").text.replace(",",""))
    CURSOR = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split()[2].replace(",", ""))
    GRANDMA = int(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split()[2].replace(",", ""))
    FACTORY = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split()[2].replace(",", ""))
    MINE = int(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split()[2].replace(",", ""))
    SHIPMENT = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split()[2].replace(",", ""))
    ALCHEMY_LAB = int(driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab b").text.split()[3].replace(",", ""))
    PORTAL = int(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split()[2].replace(",", ""))
    TIME_MACHINE = int(driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine b").text.split()[3].replace(",", ""))
    
    print(MONEY)
    if CURSOR < MONEY < GRANDMA:
        print("cursor")
        driver.find_element(By.CSS_SELECTOR, "#buyCursor b").click()
    elif GRANDMA < MONEY < FACTORY:
        # grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        print("grnad")
        driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").click()
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyGrandma b"))).click()
    elif FACTORY< MONEY <MINE:
        print("fact")
        driver.find_element(By.CSS_SELECTOR, "#buyFactory b").click()
        # WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyFactory b"))).click()
    elif MINE < MONEY < SHIPMENT:
        print("mine")
        driver.find_element(By.CSS_SELECTOR, "#buyMine b").click()
        # WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyMine b"))).click()
    elif SHIPMENT < MONEY < ALCHEMY_LAB:
        print("ship")
        driver.find_element(By.CSS_SELECTOR, "#buyShipment b").click()
        # WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyShipment b"))).click()
    elif ALCHEMY_LAB < MONEY < PORTAL:
        print("alche")
        driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab b").click()
        # WebDriverWait(driver,5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyAlchemy\ lab b"))).click()
    elif PORTAL < MONEY < TIME_MACHINE:
        print("portal'")
        driver.find_element(By.CSS_SELECTOR, "#buyPortal b").click()
        # WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyPortal b"))).click()
    elif MONEY > TIME_MACHINE:
        print("time")
        driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine b").click()
        # WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#buyTime\ machine b"))).click()
    else:
        return 0        

start = time.time()
while True:
    end_time = time.time()
    WebDriverWait(driver, 5,).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cookie"]'))).click()
    if int(end_time-start)>timeout:
        # input("wait")
        # Buy things until money does not suffieciet
        buy = best_decison()
        while  buy != 0:
            buy = best_decison()
        # time.sleep(5)
        # input("go")
        
        start = time.time()

# GAME WILL STOP AFTER 5 MINS 
    if game_timeout > 60*5:
        break



