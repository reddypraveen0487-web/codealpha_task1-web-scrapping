import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    for quote in quotes:
        print(quote.get_text())

except requests.exceptions.RequestException as e:
    print("Error:", e)