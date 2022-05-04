#it is a HTTP python library to send http requests
import requests
#it is library which will pull data from html and xml files and help navigating through parse tree
from bs4 import BeautifulSoup
#it is library use for data manipulation. for this code we used it for exporting scrapped data in csv file
import pandas as pd

#it is url from where data was scrapped.
baseurl = 'https://www.thewhiskyexchange.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}

#all srapped links are stored in this list 
product_links = []

#scrapping  all links of products from all the pages.
for x in range(1,12):
   r = requests.get(f'https://www.thewhiskyexchange.com/c/33/american-whiskey?pg={x}')
   soup = BeautifulSoup(r.content, 'lxml')
   product_list = soup.find_all('li', class_='product-grid__item')
   for item in product_list:
      for link in  item.find_all('a', href=True):
         product_links.append(baseurl + link['href'])

#printing all products links list
# print(product_links)

#it is link used for scrapping data from one product for testing
# testlink = 'https://www.thewhiskyexchange.com/p/15632/angels-envy-bourbon-port-finish'

#the data which is scrapped from code below is stored in this list
whiskylist = []
for link in product_links:
   r = requests.get(link, headers=headers)
   soup = BeautifulSoup(r.content, 'lxml')
   name = soup.find('h1', class_='product-main__name').text.strip()
   price = soup.find('p', class_='product-action__price').text.strip()
#Exception handling for products which has no rating otherwise it will crash the code   
   try:
      rating = soup.find('span', class_='review-overview__rating star-rating star-rating--50').text.strip()
   except:
      rating = 'no rating'   

#data stored in dictionary
   whisky = {
         'name': name,
         'price': price,
         'rating': rating
   }

   whiskylist.append(whisky)   
   
   print(whiskylist)   

#exporting data using pandas
df = pd.DataFrame(whiskylist, columns = ['name', 'price', 'rating'])   
df.to_csv('whiskey_brand.csv')


