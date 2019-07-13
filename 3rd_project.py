import requests
from bs4 import BeautifulSoup as BS
import os
import csv

url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
response = requests.get(url)

soup = BS(response.text, "html.parser")

tabulka1 = soup.find_all('td', {'headers': 't1sb2'})
tabulka2 = soup.find_all('td', {'headers': 't2sb2'})
tabulka3 = soup.find_all('td', {'headers': 't3sb2'})
tabulka4 = soup.find_all('td', {'headers': 't4sb2'})

tabulka1_text = []
tabulka2_text = []
tabulka3_text = []
tabulka4_text = []

for i in tabulka1:
    tabulka1_text.append(i.text)

for i in tabulka2:
    tabulka2_text.append(i.text)

for i in tabulka3:
    tabulka3_text.append(i.text)

for i in tabulka4:
    tabulka4_text.append(i.text)

print(tabulka1_text)
print(tabulka2_text)
print(tabulka3_text)
print(tabulka4_text)

cities = soup.findAll("h3", {"class": "kraj"})

# print(cities)


# mesta = tabulky.find('td',{'headers':'t2sa1 t2sb2'})
# print(mesta)

# test = response.text
# print(test)

# vysledky = open('vysledky.xml', 'wt')
# #
#
# with open('vysledky.csv', 'a') as vysledky:
#     writer = csv.writer(vysledky)
#     writer.writerow(???)
#
# vysledky.close()
