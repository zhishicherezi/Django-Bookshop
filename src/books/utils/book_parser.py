
# Парсер новых книг 

import requests
from bs4 import BeautifulSoup
import collections

URL = 'https://biblio.by/biblio-books.html'
HEADERS = {'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36',
'accept': '*/*'}

books = []

def get_html(html, params=None):
    r = requests.get(url=URL, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", {'class': 'span13 item'})
 
    for item in items:
        books.append(
            {
                'title': item.find('div', class_="product-name").get_text(),
                'price': item.find('span', class_="price").text.rstrip('\xa0руб'),
                'author': item.find('p', class_='author').text,
                'url': item.find('div', class_='product-name').find('a', href=True).get('href'),
                'img': item.find('div', class_='images-container').find('img').get('src')
            }
        )

    print(books)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print(f'Parser error, status code {html.status_code}')

parse()

