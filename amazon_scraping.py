import time
import requests

categories = [
    'laptops',
    'healthcare',
    'software',
    'baby',
    'clothing'
]

for category in categories:
    url = f'https://www.amazon.com/s?k={category}'

    # Fetch data from category
    headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        # Write the html to disk to avoid making too many requests
        with open(f'html/{category}.html', 'w', encoding='utf-8') as f:
            f.write(page.text)
        print(f'Saved {category}.html')
    else:
        print(f'{page.status_code}: Error while fetching html for {category}.')

    # Stop the program for 3 seconds before making the next request
    # This is to avoid triggering the Amazon anti-webscraping system
    time.sleep(3)