import requests
from bs4 import BeautifulSoup

def scrape_and_append_text(page_id):
    url = f'{your url here}={page_id}'

    # Add headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # Send a request to the URL with the new headers
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError for unsuccessful status codes

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h4', class_='entry-title')
        content_div = soup.find('div', class_='entry-content')

        if content_div and title:
            text_content = f'\nTitle: {title.get_text().strip()}\n'  # Include the title for reference

            # Iterate through each paragraph in the div
            for para in content_div.find_all('p'):
                for br in para.find_all('br'):
                    br.replace_with('\n')  # Replace <br> with a newline
                text_content += para.get_text() + '\n\n'  # Add two new lines after each paragraph

            # Append the extracted text to the file
            with open('extracted_text.txt', 'a', encoding='utf-8') as file:
                file.write(text_content)
            print(f"Text from '{title.get_text().strip()}' successfully appended.")
        else:
            print(f"The required elements were not found on page ID {page_id}.")

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred while accessing page ID {page_id}: {http_err}")
    except Exception as err:
        print(f"An error occurred while accessing page ID {page_id}: {err}")

# Loop through the pages
for page_id in range(4179, 4552):
    scrape_and_append_text(page_id)
