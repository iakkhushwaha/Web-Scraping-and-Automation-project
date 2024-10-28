from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
import time
from urllib.parse import urlparse

driver = webdriver.Chrome()


def get_image_name_from_url(url):
    # Parse the URL to get the path
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # Extract the image name from the path
    image_name = path.split('/')[-1]
    
    return image_name

def extract_box_1(html_content):   # Extract details for 1 box
    soup = BeautifulSoup(html_content, 'html.parser',multi_valued_attributes=None)

    # Extract the title and address
    title = soup.find('h1').text
    address = soup.find('div', class_='text-sm font-light').text

    # Extract the sections with labels
    sections = soup.find_all('div', class_='mb-4')

    texT = ""
    for section in sections:
        label = section.find('h6').text
        value = section.find('p').text
        # print(f"\n{label}\n\n{value}")
        texT = texT + f"\n{label}\n\n{value}"
    return title+"\n"+address+"\n"+texT

def extract_box_2(html_content):
    place = ''
    main_point = ''
    paragraph = ''
    try:
        soup = BeautifulSoup(html_content, 'html.parser',multi_valued_attributes=None)
        place = soup.find('div', class_="text-2xl font-bold mb-2").text
        main_point = soup.find('h2' , class_= 'md:text-xl text-lg mb-2 font-semibold').text
        paragraph = soup.find('div',class_='max-h-36 show-all project-content font-light text-sm project-description overflow-hidden relative').text
        return place+"\n"+main_point+"\n"+paragraph
    except:
        return place+"\n"+main_point+"\n"+paragraph
        
    # print(place+"\n"+main_point+"\n"+paragraph)
    # return place+"\n"+main_point+"\n"+paragraph

    
def extract_urban(html_content):
        # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser',multi_valued_attributes=None)

    # Extract the title
    feedback_title = soup.find('div', class_='font-bold text-2xl').text
    try:
    # Extract the first set of feedback items
        feedback_1_title = soup.find("div" , class_ = "text-sm my-1").text
    except:
        feedback_1_title = ''
    # feedback_1_title = f+soup.find('span', class_='font-bold').text
    try:
        feedback_1_items = soup.find_all('li', class_='py-1')
    except:
        feedback_1_items = ''
    # Extract the second set of feedback items
    
    try:
        feedback_2_title = soup.find_all('span', class_='font-bold')[1].parent.text.strip()
    except:
        feedback_2_title = ''
    try:
        feedback_2_items = soup.find_all('div', class_='text-sm mt-3 grid grid-cols-1 md:grid-cols-2')[1].find_all('li', class_='py-1')
    except:
        feedback_2_items = ''
    # Function to extract text from list items
    def extract_feedback_items(items):
        feedback_list = []
        for item in items:
            text = item.find_all('span')[0].text
            votes = item.find_all('span')[1].text
            feedback_list.append(f"{text} {votes}")
        return feedback_list

    # Extract feedback texts
    try:
        feedback_1_texts = extract_feedback_items(feedback_1_items)
    except:
        feedback_1_texts = ''
    try:    
        feedback_2_texts = extract_feedback_items(feedback_2_items)
    except:
        feedback_2_texts = ''
    text1 = ""
    text2 = ""
    # Print the extracted information
    # print(feedback_title)
    # print(feedback_1_title)
    for text in feedback_1_texts:
        # print(f"    {text}")
        text1 = text1 + f"    {text}\n"

    # print(feedback_2_title)
    for text in feedback_2_texts:
        # print(f"    {text}")
        text2 = text2 + f"    {text}\n"
    return feedback_title+"\n"+feedback_1_title+"\n"+text1+"\n"+feedback_2_title+"\n"+text2

def extract_amenities():
    element = driver.find_elements(By.CSS_SELECTOR,".bg-white.p-6.rounded-sm.border-gray-3.border.dark\:bg-slate-700.dark\:border-slate-600.dark\:text-slate-200.mt-6")
    for e in element:
        if e.text.__contains__("Amenities"):
            return e.text
def extract_amenities_tags(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser',multi_valued_attributes=None)

    # Find the amenities section
    amenities = soup.find('h2', class_='text-lg md:text-xl mb-2 font-semibold').get_text()
    all_li = soup.find_all("li" ,class_ = 'py-1')
    img_html= ""
    for i in range(len(all_li)):
        img_tag = all_li[i].find("span").find_all('img')[1]
        img_html += str(img_tag)
        
    return amenities+img_html

# def description(html_content):
#     pass

def extract_apartment():
    box = driver.find_elements(By.CSS_SELECTOR, ".bg-white.p-6.rounded-sm.border-gray-3.border.dark\:bg-slate-700.dark\:border-slate-600.dark\:text-slate-200 ")
    # print(box)
    new_apartment_sale = ""
    for b in box:
        if b.text.__contains__("New Apartments for sale"):
            new_apartment_sale = b.text
    return new_apartment_sale

def extract_town():
    box = driver.find_elements(By.CSS_SELECTOR, ".bg-white.p-6.rounded-sm.border-gray-3.border.dark\:bg-slate-700.dark\:border-slate-600.dark\:text-slate-200 ")
    # print(box)
    new_town_sale = ""
    for b in box:
        if b.text.__contains__("New Townhouses for sale"):
            new_town_sale = b.text
    return new_town_sale
            
def extract_villa():
    box = driver.find_elements(By.CSS_SELECTOR, ".bg-white.p-6.rounded-sm.border-gray-3.border.dark\:bg-slate-700.dark\:border-slate-600.dark\:text-slate-200 ")
    new_villa_sale_ = ""
    for b in box:
        if b.text.__contains__("New Villa for sale"):
            new_villa_sale_ = b.text
    return new_villa_sale_

def extract_team():
    elements  = driver.find_elements(By.CSS_SELECTOR, '.bg-white.p-6.rounded-sm.border-gray-3.border.dark\:bg-slate-700.dark\:border-slate-600.dark\:text-slate-200 ')
    for e in elements:
        if e.text.__contains__("Meet the team behind")  :
            return e.text
def extract_development(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extracting the development information
    development_info = {}
    heading = soup.find('h2',class_ = 'text-lg mb-4 font-semibold md:text-xl').text.strip()
    details_blocks = soup.find_all('div', class_='text-sm flex font-light flex')
    for d in details_blocks:
        keys = d.find_all('div', class_ = "flex-1")
        development_info[keys[0].text] = keys[1].text
    # print(development_info)
    text = heading
    for key , value in development_info.items():
        text += "\n" + key + " : " + value
    
    return text
      



def extract_project_overview(html_content):
    soup = BeautifulSoup(html_content, 'html.parser',multi_valued_attributes=None)
    title = soup.find('div', class_ = "text-xl mb-3 font-semibold").text
    paragraph = soup.find('div',class_='max-h-36 show-all project-content font-light text-sm project-description overflow-hidden relative').text
    # print(title+"\n"+paragraph)
    return title+"\n"+paragraph
    
url = "https://www.urban.com.au/new-apartments/vic-quarter-660-albany-highway-victoria-park"
def scape_data(url):
    content = requests.get(url)
    # print(content.text)
    driver.get(url)
    time.sleep(3)
    
    soup = BeautifulSoup(content.text, "html.parser",multi_valued_attributes=None)
    
    image = driver.find_element(By.XPATH,"/html/head/meta[6]")
    image_url = image.get_attribute("content")
    
    
    image_name = get_image_name_from_url(image_url)
    
    # Getting name
    # name = driver.find_element(By.XPATH,"/html/head/title").text
    name = soup.find(name="span", class_ = "dark:text-slate-400").text
    # input()
    
    
    
    
    boxes = soup.find_all(name= "div", class_ = "bg-white p-6 rounded-sm border-gray-3 border dark:bg-slate-700 dark:border-slate-600 dark:text-slate-200 ")
    boxeS = soup.find_all(name="div", class_= "bg-white p-6 rounded-sm border-gray-3 border dark:bg-slate-700 dark:border-slate-600 dark:text-slate-200 mt-6")
    parent_box = soup.find_all('div', class_= "mt-6")
    box_1 = ""
    desciption = ""
    urban = ""
    amenities_tags = ""
    amenities = ""
    devlopment = ""
    project_overview = ""
    meet_team = ""
    
    box_1 = extract_box_1(str(boxes[0]))
    desciption = extract_box_2(str(boxes[1]))
    apartment_details = extract_apartment()
    villa_details = extract_villa()    
    town_details = extract_town()  
    
    # print(apartment_details, "\n\n",villa_details)   
                
    # project_overview = extract_project_overview(str(boxes[-1]))
    
    
    
    for b in boxes:
        if b.text.__contains__("Development information"):
            devlopment = extract_development(str(b))
        if b.text.__contains__("Meet the team behind"):
            meet_team = extract_team()
        if b.text.__contains__("Project Overview"):
            project_overview = extract_project_overview(str(boxes[-1]))
            
    
    
    for b in boxeS:
        if b.text.__contains__("Urban community feedback"):
            urban = extract_urban(str(b))
        if b.text.__contains__("Amenities"):
            amenities_tags = extract_amenities_tags(str(b))
            amenities = extract_amenities()
    
    try:
        images_urls = driver.find_elements(By.CSS_SELECTOR,".object-cover")
        bulk_images_url = list(set(i.get_attribute("src") for i in images_urls))
        bulk_images_name = [get_image_name_from_url(url) for url in bulk_images_url]
    except:
        bulk_images_url = None
        bulk_images_name = None
    # EXTRACT NAME FROM IMAGES URL
    
    data = {
        "Page_URL":url,
        "Image_URL":image_url,
        "Image_Name": image_name,
        "Name": name,
        "Desccription":desciption,
        "Box_01":box_1,
        "Urban":urban,
        "Meet_Team":meet_team,
        "Amenities":amenities,
        "Amenities_html_tags":amenities_tags,
        "Development":devlopment,
        "New_Apartment_Sale": apartment_details,
        "New_Villa_Sale": villa_details,
        "New_TownHouse_Sale":town_details,
        "Project_Overview":project_overview,
        "Image_URL_bulk":bulk_images_url,
        "Image_Name_bulk":bulk_images_name
    }
    return data
