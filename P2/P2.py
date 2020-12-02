import requests
from bs4 import BeautifulSoup
infos = []
url ="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


#Initialisation de la connection de la page que nous voulons récuperer les informations.
response = requests.get(url)
if response.ok:
   soup = BeautifulSoup(response.text, 'html.parser')
   title = soup.find('title')
   

   #On fait une boucle pour récupérer toutes les balises td dans th. Puis avec l'objet string on convertit la liste en carachtére pour l'inserer dans la liste infos. 

   #description = soup.findAll(id ="product_description")
   #description = soup.find("table", {"div": 'product_description'}).find_all('p')
   #print(description)
   product_information = soup.find("table", {"class": 'table-striped'}).find_all('p')

   

   ths = soup.findAll('tr')
   for th in ths:
       th = th.find('td')
       info=th.string
       infos.append(info)
       
   print(infos)


   dscs = soup.findAll('p')
   print(dscs[4])
   for dsc in dscs:
      print(dsc)
  
