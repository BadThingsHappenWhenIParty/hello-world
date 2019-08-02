# Assignment for the task: https://drive.google.com/open?id=13wTgAOG2Ss2WtMqU6JxM9dRAYp-yUMa_

import requests
from bs4 import BeautifulSoup as BS
import os
import csv

url = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
response = requests.get(url)

soup = BS(response.text, "html.parser")
# Ignoruj ty commented-out věci, jsem to nechtěl všechno smazat, ale asi to k ničemu stejnak nebude
# print(soup.prettify())
# tabulka1 = soup.find_all('td', {'headers': 't1sb2'})
# tabulka2 = soup.find_all('td', {'headers': 't2sb2'})
# tabulka3 = soup.find_all('td', {'headers': 't3sb2'})
# tabulka4 = soup.find_all('td', {'headers': 't4sb2'})
tabulka_all = soup.find_all('td')
tabulka_all_text = []
tabulka_no_X = []
for i in tabulka_all:
    tabulka_all_text.append(i.text)

for i in tabulka_all_text:
    if i != 'X' and i != 'N':
        tabulka_no_X.append(i)
    else:
        pass

# print(tabulka_all_text)
print(tabulka_no_X)

numbers = []
names = []
for i in tabulka_no_X:
    if "CZ" in i:
        numbers.append(i)
    else:
        pass

for i in tabulka_no_X:
    if i in numbers:
        pass
    else:
        names.append(i)

print(numbers)
print(names)

my_dict = dict(zip(numbers, names))

print(my_dict)

# tabulka1_text = []
# tabulka2_text = []
# tabulka3_text = []
# tabulka4_text = []
#
# for i in tabulka1:
#     tabulka1_text.append(i.text)
#
# for i in tabulka2:
#     tabulka2_text.append(i.text)
#
# for i in tabulka3:
#     tabulka3_text.append(i.text)
#
# for i in tabulka4:
#     tabulka4_text.append(i.text)

# print(tabulka1_text)
# print(tabulka2_text)
# print(tabulka3_text)
# print(tabulka4_text)

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
