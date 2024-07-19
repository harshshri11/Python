import requests
#response = requests.get("https://www.instagram.com/")
#print(response.text)

from bs4 import BeautifulSoup
url = "https://www.instagram.com/__harsh_shrivastav__11/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
  print(heading.text)