''' Orbit objects, scrape satellite name, norad data, stay up to date '''
''' Touched base with N2YO via email, currently waiting for compiled  '''
''' JSON satellite data '''

import pathlib, requests, re
from bs4 import BeautifulSoup
import configparser, os, pathlib

base_url = 'https://www.n2yo.com/satellites/'

# Custom Header (https://httpbin.org/get)
header = {
    "Accept": "*/*",     
    "Accept-Language": "en-US,en;q=0.9", 
    "DNT": "1",        
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", 
    "Referer":"https://www.duckduckgo.com"
}

hrefs = {}

# Get repsonse data from N2YO for active objects in orbit
response = requests.get(base_url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='footable table')
for a in table.find_all('a', href=True):  
    hrefs.update({a.text:a['href']})
    #hrefs[a.text]=a['href']

# Build URL config ata
config = configparser.RawConfigParser()
# Case sensitivity
config.optionxform=str

# Orbit Objects Category
config['ORBOBJ'] = hrefs

# Save Config
with open('orbobj.ini', 'w') as configFile:
    config.write(configFile)