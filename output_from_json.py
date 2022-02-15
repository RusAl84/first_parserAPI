from bs4 import BeautifulSoup
import requests
import json


with open("headers.json", "r", encoding="utf-8") as file:
    src = json.load(file)
database = []

def output_from_json(src, database):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }

    for key in src:
        url = f"{src[key]}"
        req = requests.get(url, headers=headers)
        htmlcode = req.text
        soup = BeautifulSoup(htmlcode, "lxml")
        all_a = soup.find_all("p")

        for item in all_a:
            database.append(item.text)
        database.append("///////////////////////////////////////////////////")

output_from_json(src, database)

for text in database:
    print(text)


