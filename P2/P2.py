import requests
import csv
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

   infos.append(soup.find('div',{'class':'item active'}).find('img')['src'])
   

   print(infos)
   
with open("information.csv","w",newline="") as f:
    ecriture = csv.writer(f)
    ecriture.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    ecriture.writerow([url, infos[0], infos[1], infos[2], infos[3], infos[4], infos[5]])