import requests  
# bs4 helps decode and search through page.                                            
from bs4 import BeautifulSoup as bs                                         

# The User-Agent request header contains a characteristic string 
# that allows the network protocol peers to identify the application type, 
# operating system, and software version of the requesting software user agent.
# needed for google search
u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details

# For making individual page URLS


# Create Soup object with bs4
def soupee(url):          
  response = requests.get(url, headers=u_agnt)  
  html = response.text #To get actual result i.e. to read the html data in text mode                                                
  soup = bs(html, 'html.parser')
  return soup

# Parse page and create three lists of the headline,Description and images
# to each news of title
def parser(soup):   
  headlines = []
  Desc = []   

  for heading in soup.find_all('div', class_='ContentRoll__Headline'):
    headlines.append(heading.h2.text)

  for desc in soup.find_all('div',class_='ContentRoll__Desc'):
    Desc.append(desc.text)

  return headlines,Desc

                                    

