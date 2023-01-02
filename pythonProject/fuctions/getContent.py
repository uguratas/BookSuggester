import csv
from _csv import writer

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import json

def content(search_term):
    bookInfos = []
    for x in range(0, 1):
        my_url = "https://www.kitapyurdu.com/index.php?route=product/search&page={}&filter_name={}".format(x, search_term)

        links = []
        client = uReq(my_url)
        page_html = client.read()
        client.close()
        page_soup = soup(page_html,"html.parser")
        book_link = page_soup.findAll('a', {"class": "pr-img-link"})

        for link in book_link:
            links.append(link.get('href'))


        with open("info.csv", 'w', encoding='utf8', newline='') as f:
            theWriter = csv.writer(f,quotechar=' ', quoting=csv.QUOTE_ALL)

            for i in range(0, len(links)):

                my_url2 = links[i]
                prices = []
                pictures = []
                names = []
                authors = []
                infos = []
                client2 = uReq(my_url2)
                page_html2 = client2.read()
                client2.close()
                page_soup2 = soup(page_html2)

                book_price = page_soup2.findAll('div', {"class": "price__item"})
                book_name = page_soup2.findAll('div', {"class": "pr_header"})
                #book_pictures = page_soup2.find('a',{"class":"js-jbox-book-cover"})
                book_author = page_soup2.findAll('a', {"class": "pr_producers__link"})
                book_info = page_soup2.findAll('span', {"class": "info__text"})
                for item in book_info:
                    infos.append(item.text.replace('\n',''))

                #for link in book_pictures:
                    #pictures.append(link.get('src'))
                for item in book_price:
                    prices.append((item.text.replace(' ','')))

                for item in book_name:
                    names.append(item.text.replace('\n',''))

                for item in book_author:
                    authors.append(item.text.replace(' ',''))

                bosluk = ["--------------"]
                theWriter.writerow(names)
                bookInfos.append(names)
                theWriter.writerow(prices)
                names.append("-".join(prices))
                theWriter.writerow(authors)
                names.append("-".join(authors))
                #theWriter.writerow(pictures)
                #names.append("-".join(pictures))
                    #Bazı kitapların resimlerini almakta hata aldığımız için kitap resimleri yorum satırında bulunuyor.
                    #İlerleyen dönemde hata çözülecek.
                theWriter.writerow(infos)
                names.append("-".join(infos))
                theWriter.writerow(bosluk)

    return bookInfos