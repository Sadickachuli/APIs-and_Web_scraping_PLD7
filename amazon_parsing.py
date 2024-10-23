from bs4 import BeautifulSoup
import requests
import re

categories = [
    'laptops',
    'healthcare',
    'software',
    'baby',
    'clothing'
]

# Method to sanitize filenames for saving in windows
def sanitize_filename(filename):
    # Replace unsafe characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

for category in categories:
    with open(f'html/{category}.html', encoding='utf-8') as f:
        # Read the HTML from file
        html = f.read()

        # Parse the HTML using Beutiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Extract the first product on the page
        products = soup.find_all(attrs={"data-component-type": 's-search-result'})
        first_product = products[0]

        # Extract the image source
        image_src = first_product.find('img')['src']

        # Extract the title
        title = first_product.find('h2').get_text(strip=True)

        # Fetch the image
        headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
        request = requests.get(image_src, headers=headers)

        if request.status_code == 200:
            # Read the image data
            image = request.content

            # Create a file path for the image
            image_file_path = (f'imgs/{sanitize_filename(title)}.jpg')

            # Write the image to disk
            with open(image_file_path, 'wb') as f:
                f.write(image)

            print(f'Saved {image_file_path}')
        else:
            print(f'Something went wrong reading image for category {category}.')
        
