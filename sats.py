import pathlib, requests, re
from bs4 import BeautifulSoup

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

response = requests.get(base_url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
for a in soup.find_all('a', href=True):
    if '?c=' in re.sub('[^?c=0-9]', '', a['href']):
        hrefs[re.sub('^[\s]+','',a.text)]=re.sub('[^?c=0-9]', '', a['href'])

for k, v in hrefs.items():
    print(f'Key: {k} Value: {v}')
        #response = requests.get(base_url+a['href'], headers=header)
        #soup = BeautifulSoup(response.text, 'html.parser')
