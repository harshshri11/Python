import requests

def get_news(api_key, topic):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "q": topic,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    api_key = "cd86a5812dcd4af48197ae2cac9417bf"
    topic = input("Enter the topic you want:")
    news_data = get_news(api_key, topic)

    if news_data:
        articles = news_data["articles"]
        for article in articles:
            title = article["title"]
            source = article["source"]["name"]
            url = article["url"]
            print(f"{title} - {source} /n")
            print(f"{url}")
            print("")
    else:
        print("No news data available.")
