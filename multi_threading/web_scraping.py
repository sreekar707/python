import threading
import requests
from bs4 import BeautifulSoup
import json

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

data = []

def content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    data.append({
        "url": url,
        "content": soup.text.strip()
    })
    # print(f"Fetched content from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All URLs fetched")
json_data = json.dumps(data, indent=4)
print(json_data)
with open('langchain_data.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("JSON data has been saved to 'langchain_data.json'")