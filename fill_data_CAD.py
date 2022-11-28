from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import re
import os
from selenium.webdriver.chrome.options import Options
import generate_email

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)

username = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("LINKEDIN_PASS")
n = 1

PATH = "/Users/mac/Desktop/Projects/Email Script/chromedriver"
column_names = ["Name", "Company", "Location", "Email"]
name = None
email = None
company = None
location = None
file_name = "Email_Formats.xlsx"

df = pd.DataFrame(columns=column_names)

current_page = "1"

url = f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%22418095%22%2C%221612748%22%2C%223253035%22%2C%222812971%22%2C%2211201714%22%2C%2220226%22%2C%22468160%22%2C%2212096%22%2C%221419%22%2C%225208813%22%2C%221344398%22%2C%222281490%22%2C%221767%22%2C%223205050%22%2C%221328202%22%2C%222922%22%2C%22102661%22%2C%22167907%22%2C%22316525%22%2C%22482819%22%2C%2222883%22%2C%22212669%22%2C%22400528%22%2C%223608%22%2C%222453129%22%2C%2233223%22%2C%224929%22%2C%225128%22%2C%2218505670%22%2C%221879%22%2C%22926041%22%2C%223018203%22%2C%222017%22%2C%221482%22%2C%2280086817%22%2C%22675562%22%5D&geoUrn=%5B%22104116203%22%2C%22102277331%22%2C%22101174742%22%2C%22105149290%22%2C%2290009551%22%2C%22103644278%22%2C%22100025096%22%5D&industry=%5B%226%22%2C%224%22%5D&origin=FACETED_SEARCH&page={current_page}&sid=%2CAq"
starting_url = "https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3FcurrentCompany%3D%255B%25221035%2522%252C%25221441%2522%252C%25223185%2522%252C%25222775%2522%252C%2522784652%2522%252C%25221586%2522%252C%25221808%2522%252C%25223139%2522%252C%25222587%2522%252C%25221063%2522%252C%25221815218%2522%252C%2522314350%2522%252C%25221066442%2522%252C%25221337%2522%252C%25221482%2522%252C%252219022%2522%252C%25222017%2522%252C%2522207470%2522%252C%25222494%2522%252C%25222620735%2522%252C%2522309694%2522%252C%25223477522%2522%252C%2522433549%2522%252C%2522675562%2522%255D%26geoUrn%3D%255B%2522103644278%2522%252C%2522105149290%2522%255D%26industry%3D%255B%25224%2522%252C%252296%2522%255D%26origin%3DFACETED_SEARCH%26page%3D1%26schoolFilter%3D%255B%2522220671%2522%252C%2522166689%2522%255D%26sid%3DYPw&fromSignIn=true&trk=cold_join_sign_in"
driver.get(starting_url)
user = driver.find_element(By.ID, "username")
user.send_keys(username)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

finished = input("Did you finish security check? ")
if finished == "yes":
    print("proceeding...")

# new page
driver.get(url)
curr_page = driver.page_source
doc = BeautifulSoup(curr_page, "html.parser")

major = doc.find(
    ["div"], class_="search-marvel-srp")

for i in range(1,101):
    current_page = str(i)
    url = f"https://www.linkedin.com/search/results/people/?currentCompany=%5B%22418095%22%2C%221612748%22%2C%223253035%22%2C%222812971%22%2C%2211201714%22%2C%2220226%22%2C%22468160%22%2C%2212096%22%2C%221419%22%2C%225208813%22%2C%221344398%22%2C%222281490%22%2C%221767%22%2C%223205050%22%2C%221328202%22%2C%222922%22%2C%22102661%22%2C%22167907%22%2C%22316525%22%2C%22482819%22%2C%2222883%22%2C%22212669%22%2C%22400528%22%2C%223608%22%2C%222453129%22%2C%2233223%22%2C%224929%22%2C%225128%22%2C%2218505670%22%2C%221879%22%2C%22926041%22%2C%223018203%22%2C%222017%22%2C%221482%22%2C%2280086817%22%2C%22675562%22%5D&geoUrn=%5B%22104116203%22%2C%22102277331%22%2C%22101174742%22%2C%22105149290%22%2C%2290009551%22%2C%22103644278%22%2C%22100025096%22%5D&industry=%5B%226%22%2C%224%22%5D&origin=FACETED_SEARCH&page={current_page}&sid=%2CAq"
    driver.get(url)
    curr_page = driver.page_source
    doc = BeautifulSoup(curr_page, "html.parser")
    major = doc.find(["div"], class_="ph0 pv2 artdeco-card mb2").ul

    people = major.find_all("li")

    for p in people:
        try:
            name = p.find("div", class_="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex")
            name = name.find("img", alt=True)['alt'].lower()
        except:
            print("Name failed")
            name = None

        try:
            company = p.find("div", class_="entity-result__primary-subtitle t-14 t-black t-normal").get_text().replace("\n", "").replace("@", "").lower()
        except:
            print("Company Failed")
            company = None

        try:
            location = p.find("div", class_="entity-result__secondary-subtitle t-14 t-normal").get_text().lower()
        except:
            print("location failed")
            location = ""

        if name and company:
            email = generate_email.generate_email(name, company)
        else:
            email = "N/A"

        print(name, company, location, email)
        if name:
            df.loc[n] = [name, company, location, email]
        n += 1
    df.to_excel("CAD_Data.xlsx", index=False)


df = pd.DataFrame(columns=column_names)