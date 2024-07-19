import requests
import json

query = input("What type of news do you want to see: ")
url = f"https://newsapi.org/v2/everything?q={query}&apiKey=cd86a5812dcd4af48197ae2cac9417b"
r = requests.get(url)
news = json.loads(r.text)

for article in news["articles"]:
  print(article["title"])
  print(article["description"])
  print("")
