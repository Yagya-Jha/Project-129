import pandas as pd
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time
import csv
import requests

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)

# time.sleep(10)

header = ["Name", "Distance", "Mass", "Radius"]
star_data = []

def scraep():

    soup = bs(page.text, "html.parser")
    star_table = soup.find_all('table')
    table_rows = star_table[7].find_all("tr")
    temp_list = []
    for i in table_rows:
        td=i.find_all("td")
        row=[i.text.rstrip() for i in td]
        temp_list.append(row)

    name = []
    distance = []
    mass = []
    radius = []

    for i in range(1, len(temp_list)):
        if not temp_list[i][0] == "" and not temp_list[i][5] == "" and not temp_list[i][7] == "" and not temp_list[i][8] == "":
            name.append(temp_list[i][0])
            distance.append(temp_list[i][5])
            mass.append(float(temp_list[i][7])*0.000954588) #convert to solar mass.
            radius.append(float(temp_list[i][8])*0.102763) #convert to solar radius.

    df = pd.DataFrame(list(zip(name, distance, mass, radius)), columns=header)
    df.to_csv('scrapper_1.csv')

scraep()