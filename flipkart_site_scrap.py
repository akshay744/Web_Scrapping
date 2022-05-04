#it is library which will pull data from html and xml files and help navigating through parse tree.
from bs4 import BeautifulSoup
#it is a HTTP python library to send http requests.
import requests
#it is use to read or write data in csv format.
from csv import writer

#it is a url from data was scrapped
url = "https://www.flipkart.com/search?q=camera&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=camera%7CDSLR+%26+Mirrorless&requestId=8501756a-a685-49b7-a067-3f106bc3ef31&as-searchtext=camer"

r = requests.get(url)

htmlcontent = r.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

#to export file in csv format
# with open('product_flip.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ['Title', 'Price', 'image']
#     thewriter.writerow(header)

#it is scrapping the title, price and image link of products on page 1.
for d in soup.find_all('div', attrs={'class':'_2kHMtA'}):
    title = d.find('div', attrs={'class':'_4rR01T'}).string
    price = d.find('div', attrs={'class':'_30jeq3 _1_WHN1'}).string
    image = d.find('img', attrs={'class':'_396cs4 _3exPp9'}).get('src')       
    info = [title, price, image]

        # thewriter.writerow(info)

    print(info)


