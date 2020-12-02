import requests
from bs4 import BeautifulSoup
infos = []
url ="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


#Initialisation de la connection de la page que nous voulons récuperer les informations.
response = requests.get(url)
if response.ok:
   soup = BeautifulSoup(response.text, 'html.parser')
   title = soup.find('title')
   infos.append(title.string)
   
   ths = soup.findAll('tr')
   for th in ths:
       th = th.find('td')
       infos.append(th.string)

   dscs = soup.findAll('p')
   infos.append(dscs[3])

   print(infos)
  
  
