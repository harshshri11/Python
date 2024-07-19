import concurrent.futures
import requests


def downloadFile(url, name):
    try:
        print(f"Started Downloading {name}")
        response = requests.get(url)
        file_path = f"files/file{name}.jpg"
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Finished Downloading {name}")
        return f"Downloaded {name}"
    except Exception as e:
        return f"Error downloading {name}: {e}"


def main():
    url = "https://picsum.photos/2000/3000"
    max_workers = 5  # Adjust based on your system's capabilities
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        urls = [url for _ in range(60)]
        indexes = [i for i in range(60)]
        results = executor.map(downloadFile, urls, indexes)

        for r in results:
            print(r)


if __name__ == "__main__":
    main()
