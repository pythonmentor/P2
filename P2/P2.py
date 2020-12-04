import requests
import csv
from bs4 import BeautifulSoup
infos = []
host = 'http://books.toscrape.com/catalogue/'
url ="http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
url2 ="http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
livres= []
nbrdepage = []

def scraping (url):
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
 
               if (th.string == "Price (excl. tax)") or (th.string == "Price (incl. tax)"):
                   infos.append(td.string[2:])
               elif th.string == "Availability":
                   infos.append(td.string[10:-11])
               else: infos.append(td.string)

  
      infos.append(soup.findAll('p')[3]) #Ajout de la déscription


      infos.append(url + soup.find('div',{'class':'item active'}).find('img')['src'][5:]) #Ajout du lien de l'image 
   
   


   with open("information.csv","w",newline="") as f:
       ecriture = csv.writer(f)
       ecriture.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
       ecriture.writerow([infos[0], infos[3], infos[1], infos[4], infos[5], infos[6], infos[8], infos[2], infos[7], infos[9]])

       [print(str([i]) + '\n') for i in infos]

  


def scan ():
   response = requests.get(url2)
   if response.ok:
          soup = BeautifulSoup(response.text, 'html.parser')
          livre = soup.find('div',{'class':'col-sm-8 col-md-9'}).findAll('div', {'class':'image_container'})
          for i in livre:
             livres.append(host + i.find('a')['href'][9:])
          
       
          print(livres)
 
def scan_page ():
   response = requests.get("http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html")
   if response.ok:
      soup = BeautifulSoup(response.text, 'html.parser')
      rslt = soup.find('ul',{'class':'pager'})
      for i in rslt:
           #i.find('li', {'class':'next'}) 
           print(i)
      print(rslt)


scan_page()