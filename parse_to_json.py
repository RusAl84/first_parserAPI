import requests
import time
from bs4 import BeautifulSoup
import json

print("Enter your key words right down below")
keywords = []
for i in input().split():
    y = str(i)
    keywords.append(y)


first_page_number = int(input("Enter pages of site you want to parse\nFirst page number: "))
second_page_number = int(input("Second page number: "))
database = {}

def simple_parser_with_keywords(first_page_number, second_page_number, database, keywords):
    for number in range(first_page_number, second_page_number + 1):
        if number == 0:
            url = "https://cryptonews.net/ru/"
        else:
            url = "https://cryptonews.net/ru/" + f"page-{number}/"
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }

        # Получение и запись HTML-кода страницы
        req = requests.get(url, headers=headers)
        src = req.text

        soup = BeautifulSoup(src, "lxml")

        # Поиск всех заголовков статей
        all_a = soup.find_all("a", class_="title")
        temp_database = {}

        # Создание словаря типа {Ссылка на статью: заголовок статьи}
        for item in all_a:
            item_text = item.text
            item_url = "https://cryptonews.net" + item.get("href")
            temp_database[item_text] = item_url

        # for key in temp_database:
        #     print(key)
        if not keywords:
            for key in temp_database:
                database[key] = temp_database[key]
        else:
            for text in temp_database:
                for keyword in keywords:
                    if keyword in text:
                        database[text] = temp_database[text]


simple_parser_with_keywords(first_page_number, second_page_number, database, keywords)


with open("headers.json", "w", encoding="utf-8") as file:
    json.dump(database, file, indent=4, ensure_ascii=False)
