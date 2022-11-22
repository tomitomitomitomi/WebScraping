from bs4 import BeautifulSoup
import requests
import re

data = requests.get('https://www.alavus.fi/fi/kaupunki-ja-hallinto/asiointi.html')
#print(data.content)

soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())

print('Linkkitagit:')
for li in soup.find_all('li'):
    print(li)

#normi regex scraping:
print('Sähköpostiosoitteet:')
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)
print(emails)
