import requests
from bs4 import BeautifulSoup
headers = {
    "Host": "mill.com",
}
res = requests.get('http://localhost:8000/', headers=headers)
print(res)

soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())