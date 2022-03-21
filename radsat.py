import pathlib, requests, re, configparser
from bs4 import BeautifulSoup

# N2Y0 Base URL for satellite data
base_url = 'https://www.n2yo.com/satellites/'

# Read Orb Obj parameters
param = configparser.ConfigParser()
param.read('orbobj.ini')

# Custom Header (https://httpbin.org/get)
header = {
    "Accept": "*/*",     
    "Accept-Language": "en-US,en;q=0.9", 
    "DNT": "1",        
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36", 
    "Referer":"https://www.duckduckgo.com"
}

satellites = {}

for section in param.sections():
    if section == 'ORBOBJ':
        for obj, parameter in param.items(section):
            #print(base_url+parameter)
            # Pass parameters from ini
            
            response = requests.get(base_url+parameter, headers=header)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Scrape satellite data
            for row in soup.find_all('tr'):
                for a in row.find_all('a', href=True):  
                    if '/satellite/' in a['href']:
                        # Extract href, clean URL, includes NORAD ID + Title
                        link = re.sub('\/[\w]+\/','', a['href'])
                        satellites.update({a.text:link})                        

# Build URL config ata
config = configparser.RawConfigParser()
# Case sensitivity
config.optionxform=str

# Orbit Objects Category
config['RADSATS'] = satellites

# Save Config
with open('radsats.ini', 'w') as configFile:
    config.write(configFile)