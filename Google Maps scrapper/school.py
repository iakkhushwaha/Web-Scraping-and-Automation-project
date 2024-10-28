from selenium import webdriver
from selenium.webdriver.common.by import By



def search_place(url):
    driver = webdriver.Chrome()

    driver.get(url)
    # input()

    name = driver.find_element(By.CSS_SELECTOR, ".lfPIob").text
    print(name)
    try:
        address = driver.find_element(By.CSS_SELECTOR, "div.RcCsl:nth-child(3) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").text
        print(address)
    except:
        pass
    try:
        website = driver.find_element(By.CSS_SELECTOR, "a.CsEnBe").get_attribute("href")
        print(website)
    except:
        pass
    try:
        phone = driver.find_element(By.CSS_SELECTOR, 'div.RcCsl:nth-child(6) > button:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)').text.replace(" ", "")[1:]
        print(phone)
    except:
        pass


# input()
