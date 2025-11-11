thonimport requests
from bs4 import BeautifulSoup

def parse_facebook_page(url):
    """Parse a Facebook page and extract contact information."""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    
    contact_info = {}
    contact_info['address'] = soup.find('meta', {'property': 'og:location'})['content'] if soup.find('meta', {'property': 'og:location'}) else ''
    contact_info['email'] = soup.find('a', {'href': 'mailto:'})['href'][7:] if soup.find('a', {'href': 'mailto:'}) else ''
    contact_info['phone'] = soup.find('a', {'href': 'tel:'})['href'][4:] if soup.find('a', {'href': 'tel:'}) else ''
    contact_info['website'] = soup.find('a', {'rel': 'nofollow'})['href'] if soup.find('a', {'rel': 'nofollow'}) else ''
    
    return contact_info