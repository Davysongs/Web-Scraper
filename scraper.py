import requests
from bs4 import BeautifulSoup
import time

product = input('Enter the name of the product: ')
page_limit = int(input('Enter the page limit: '))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def productsResearch(product, page):
    url = f'https://www.jumia.com.ng/catalog/?q={product}&page={page}#catalog-listing'
    try:
        jumia_url = requests.get(url, headers=headers)
        jumia_url.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(jumia_url.text, 'lxml')
        phones = soup.find_all('article', {'class': 'prd _fb col c-prd'})

        for phone in phones:
            try:
                phone_price = phone.find('div', {'class': 'prc'}).text
                phone_details = phone.find('h3', {'class': 'name'}).text
                phone_rating = phone.find('div', {'class': 'rev'}).text
                link = 'https://www.jumia.com.ng/catalog' + \
                    phone.find('a', {'class': 'core'})['href']
                print(f'Phone details: {phone_details}')
                print(f'Phone price: {phone_price}')
                print(f'Phone rating: {phone_rating}')
                print(f'Purchase link: {link}')
                print('')
            except Exception as e:
                print('No review for this product')
    except requests.RequestException as e:
        print(f'Error accessing the page: {e}')

for i in range(1, page_limit):
    productsResearch(product, i)

time_wait = 10
print(f'Waiting {time_wait} minutes')
time.sleep(time_wait * 60)
