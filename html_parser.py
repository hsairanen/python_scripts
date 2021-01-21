# VERSION 1

import re
import urllib.request
import sys


URL = "http://personal.lut.fi/"
page = urllib.request.urlopen(URL)
data = page.read().decode("utf-8")
page.close()

data = re.sub( '<[^<]+?>', ' ', data)
    
# Kirjoita data
try:
    tiedosto = open("htulos.txt", "w")
except OSError:
    print(f"Tiedoston '{tiedostonimi}' avaaminen epäonnistui.")
    sys.exit(0)
     
try:
    tiedosto.write(data)
except OSError:
    print("Tiedoston '{tiedostonimi}' kirjoittaminen epäonnistui.")
    sys.exit(0)
 
tiedosto.close()
    

#%%

# VERSION 2

import requests
from bs4 import BeautifulSoup

URL = "http://personal.lut.fi/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
# or
# soup = BeautifulSoup(page.text, 'xml').text

print(soup.prettify())

# Find a title
title = soup.find('title') 

print(title.string)

# Find all h1s

h1s = soup.find_all('h1')

for i in h1s:
    print(i.string)