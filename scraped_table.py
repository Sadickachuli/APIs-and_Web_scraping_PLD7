import requests
from bs4 import BeautifulSoup
import csv

# Base URL with placeholder for the page number
base_url = 'https://www.scrapethissite.com/pages/forms/?page_num='

# Number of pages to scrape (you can change this to scrape more pages)
num_pages_to_scrape = 4

# Prepare CSV file to store data from all pages
with open('scraped_table_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    header_written = False  # Flag to write headers only once

    # Loop through the page numbers
    for page_num in range(1, num_pages_to_scrape + 1):
        # Construct the full URL for the current page
        url = base_url + str(page_num)
        print(f'Scraping page {page_num}: {url}')

        # Send HTTP request to the current page URL
        response = requests.get(url)

        # Create BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table
        table = soup.find('table', class_='table')

        # Get all rows from the table
        rows = table.find_all('tr')

        # Write headers from the first row (only once)
        if not header_written:
            header = [th.text.strip() for th in rows[0].find_all('th')]
            writer.writerow(header)
            header_written = True  # Avoid writing headers again

        # Write the remaining rows
        for row in rows[1:]:
            data = [td.text.strip() for td in row.find_all('td')]
            writer.writerow(data)

print("Tabular data from multiple pages saved in scraped_table_data_multiple_pages.csv")
