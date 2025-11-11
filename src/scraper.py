thonimport requests
from bs4 import BeautifulSoup
import json
import csv

def fetch_facebook_page(url):
    """Fetch the content of a Facebook page."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def extract_contact_info(page_html):
    """Extract contact information from a Facebook page."""
    soup = BeautifulSoup(page_html, 'html.parser')
    contact_info = {
        'address': '',
        'email': '',
        'phone': '',
        'likes': 0,
        'website': '',
        'checkins': 0
    }
    
    # Example of extracting data from meta tags or specific HTML elements (adjust accordingly)
    contact_info['address'] = soup.find('meta', {'property': 'og:location'})['content'] if soup.find('meta', {'property': 'og:location'}) else ''
    contact_info['email'] = soup.find('a', {'href': 'mailto:'})['href'][7:] if soup.find('a', {'href': 'mailto:'}) else ''
    contact_info['phone'] = soup.find('a', {'href': 'tel:'})['href'][4:] if soup.find('a', {'href': 'tel:'}) else ''
    contact_info['likes'] = int(soup.find('div', {'class': '_4bl9'}).text) if soup.find('div', {'class': '_4bl9'}) else 0
    contact_info['website'] = soup.find('a', {'rel': 'nofollow'})['href'] if soup.find('a', {'rel': 'nofollow'}) else ''
    contact_info['checkins'] = int(soup.find('div', {'class': '_5g-i'}).text) if soup.find('div', {'class': '_5g-i'}) else 0
    
    return contact_info

def save_to_json(data, filename='contact_info.json'):
    """Save extracted contact information to a JSON file."""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def save_to_csv(data, filename='contact_info.csv'):
    """Save extracted contact information to a CSV file."""
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    url = input("Enter Facebook page URL: ")
    page_html = fetch_facebook_page(url)
    contact_info = extract_contact_info(page_html)
    
    save_to_json(contact_info)
    save_to_csv([contact_info])
    print("Contact information saved!")