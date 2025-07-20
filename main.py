import requests
from bs4 import BeautifulSoup


url = 'https://www.superprof.ma/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

header_text = soup.find("h1").get_text(strip=True)


print("Original:", header_text)
