import requests
import csv
from bs4 import BeautifulSoup
infos = []
url ="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


#Initialisation de la connection de la page que nous voulons récuperer les informations.
response = requests.get(url)
if response.ok:
   soup = BeautifulSoup(response.text, 'html.parser') 
   infos.append(url) #On ajoute l'URL
   infos.append(soup.find('li', {'class':'active' } ).string) #On ajoute le titre
   infos.append(soup.find('ul', {"class":"breadcrumb"}).findAll('li')[2].find('a').string) #On ajoute la catégorie



   #Ajout des autres informations qui sont dans les <td> en discriminant les <tr> contenant Product type et Tax. 

   trs = soup.findAll('tr')
   for tr in trs:     
        th = tr.find('th')
        td = tr.find('td')
        if (th.string != "Product Type") and (th.string !="Tax"):
           infos.append(td.string)
           

  
   infos.append(soup.findAll('p')[3]) #Ajout de la déscription


   infos.append(soup.find('div',{'class':'item active'}).find('img')['src']) #Ajout du lien de l'image 
   
   
with open("information.csv","w",newline="") as f:
    ecriture = csv.writer(f)
    ecriture.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
    ecriture.writerow([infos[0], infos[3], infos[1], infos[4], infos[5], infos[6], infos[8], infos[2], infos[7], infos[9]])

    [print(str([i]) + '\n') for i in infos]