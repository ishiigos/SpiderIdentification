import requests
from bs4 import BeautifulSoup
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas


siteUrl = "https://araneae.nmbe.ch/matrixlinkey"
# For obtaining species name
driver = webdriver.Chrome()
driver.get(siteUrl)
soup5 = BeautifulSoup(driver.page_source, 'html.parser')

test_compiled = []


num = 1
while num < 1532:
    print("Number at the start of the while loop is ", num)
    testURL = f"https://araneae.nmbe.ch/matrixlinkey/getchar?speciesId={num}"

    species_dict = {}
    page = requests.get(testURL, verify=False)
    classdesc = page.content
    # time.sleep(1)

    # For Cleaning Species content
    pageContentString = str(classdesc).replace("\\", "").replace('<p class="specDesc">', '').replace(
        '</p></p>', '</p>').replace('b''\\"charString\\":\\"</p>\\"', '').replace('"</p>', '" </p>').replace("</p>", " </p>")

    trial = pageContentString[1:].split()[0]
    pageContentString1 = pageContentString.replace(trial, "").replace("b ", "")
    trial1 = pageContentString1.split()[0]
    trial2 = pageContentString1[5:].split()[0]
    try:
        p = pageContentString1.split()[3]
        p1 = p.split(">")[0]
        p2 = p.split(">")[1]
    except:
        species = soup5.find('li', id=f's_{num}')
        species_name = list(species.children)[1]
        species_dict["species name"] = species_name
        test_compiled.append(species_dict)
        num = num + 1
    else:
        length = len(pageContentString1)
        delimited = pageContentString1.split(" </p>")

        for cont in delimited:
            cont1 = cont.split("==>")
            len(cont1)
            if len(cont1) == 2:
                key = cont1[0]
                values = cont1[1]
                species_dict[f"{key}"] = values
            else:
                species = soup5.find('li', id=f's_{num}')
                species_name = list(species.children)[1]
                species_dict["species name"] = species_name
        test_compiled.append(species_dict)
        num = num + 1
        print("num at the end of the loop is", num)
        time.sleep(2)
print(test_compiled)

df = pandas.DataFrame.from_records(test_compiled)

print(df)


df.to_excel('Testing123.xlsx', index=False)
