import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://www.proprjeta.com/Property/Buy'

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.proprjeta.com/Property/Buy")

elem =WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//li[@class='page']/a[text()='3']")) #This is a dummy element
).click()
time.sleep(10)
html = driver.page_source
soup = BeautifulSoup(html,features="lxml")
smt = driver.find_element(By.XPATH, "//body").get_attribute('outerHTML')
print(smt)
#<li class="next"><a href="#">&gt;</a></li>sapt19159