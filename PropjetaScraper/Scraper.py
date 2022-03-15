from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import lxml.html
from selenium.common.exceptions import TimeoutException
import json

url = 'https://www.proprjeta.com/Property/Buy'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# configure webdriver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-logging"])


i = 1
list_of_inner_text = []
properjetaList = []
nextPageAvailable = True
driver = webdriver.Chrome(options=options)
driver.get("https://www.proprjeta.com/Property/Buy")

while nextPageAvailable:
    try:
        # Fetch eleemnts' texts
        elem =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@class='page']/a[text()='" + str(i + 1) + "']"))
        ).click()
        sleep(5)
        soup = BeautifulSoup(driver.page_source,features="lxml")
        propertyDataRawTitle = soup.find_all("h4",class_= "property-title")
        propertyDataRawPrice = soup.find_all("span",class_= "price")
        propertyDataRawStatus = soup.find_all("span",class_= "property-status")
        propertyLink = soup.findAll(href=True, class_="property-lnk")
   
        
        for x in range(len(propertyDataRawTitle) - 1):
            # Create a dictionary
            property = {"Title": propertyDataRawTitle[x].get_text(), "Price": propertyDataRawPrice[x].get_text(), "Status":  propertyDataRawStatus[x].get_text(), "Link": propertyLink[x]["href"]}
            properjetaList.append(property)

        i = i + 1
        
    except TimeoutException:
        print("Page" + str(i) + "did not manage to load.")
        nextPageAvailable = False
    
with open('propjetaResult.json', 'w', encoding='utf-8') as f:
    json.dump(properjetaList, f)