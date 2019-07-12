import requests
from bs4 import BeautifulSoup as BS
import os
import csv

response = requests.get("https://https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ")

soup = BS(response.text, "html.parser")
print(soup)
test = response.text

# vysledky = open('vysledky.csv', 'wt')
#
# first_row = ['cislo','nazev','celkem','v %']
# with open('vysledky.csv', 'a') as vysledky:
#     writer = csv.writer(vysledky)
#     writer.writerow(first_row)

vysledky.close()
