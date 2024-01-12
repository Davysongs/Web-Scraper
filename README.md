# Jumia Product Scraper

## Overview

This Python script scrapes product information from the Jumia website based on user input. It extracts details such as price, product details, rating, and purchase links for a specified product.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`

Install the required packages using:

```bash
pip install requests beautifulsoup4

# Jumia Product Scraper

## Overview

This Python script scrapes product information from the Jumia website based on user input. It extracts details such as price, product details, rating, and purchase links for a specified product.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`, `beautifulsoup4`

Install the required packages using:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Run the script:

    ```bash
    python jumia_scraper.py
    ```

2. Enter the name of the product and the desired page limit when prompted.

3. The script will fetch information from Jumia for each page within the specified limit.

4. The extracted details will be displayed, including product details, price, rating, and purchase link.

## Important Note

Ensure compliance with Jumia's terms of service and policies. Web scraping may be subject to legal and ethical considerations.

## Customization

Feel free to customize the script to meet your specific needs. Possible improvements include adding error handling, adjusting the time delay, or enhancing the user interface.


## Acknowledgments

- This script was created for educational purposes and should be used responsibly.
- Special thanks to Jumia for providing product information.

```

This Python script uses the `requests` and `BeautifulSoup` libraries to scrape product information from the Jumia website. It takes two user inputs: the name of the product to search for and the number of pages of results to scrape.

## Step-by-Step Explanation

### 1. Import Necessary Libraries

```python
import requests
from bs4 import BeautifulSoup
import time
```

### 2. Get User Input

The script prompts the user to enter the name of the product they want to search for and the number of pages of results they want to scrape.

```python
product = input('Enter the name of the product: ')
page_limit = int(input('Enter the page limit: '))
```

### 3. Set Request Headers

The script sets the `User-Agent` header to mimic a web browser, which is necessary for making requests to the Jumia website.

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
```

### 4. Define the `productsResearch` Function

The `productsResearch` function takes two arguments: the product name and the page number. It constructs the URL for the Jumia product search page, including the product name and page number.

```python
def productsResearch(product, page):
    url = f'https://www.jumia.com.ng/catalog/?q={product}&page={page}#catalog-listing'
```

### 5. Make the Request and Parse the HTML

The function makes a GET request to the URL using the `requests` library. If the request is successful, it uses `BeautifulSoup` to parse the HTML response.

```python
    try:
        jumia_url = requests.get(url, headers=headers)
        jumia_url.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(jumia_url.text, 'lxml')
```

### 6. Extract Product Information

The function then extracts the product information from the parsed HTML. It finds all the product articles on the page
