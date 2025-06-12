import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.parse import Quote  # Assuming Quote has attributes: text, author, tags


BASE_URL = "https://quotes.toscrape.com"


def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def parse_quotes_from_page(soup):
    quotes = []
    for quote_div in soup.select(".quote"):
        text = quote_div.select_one(".text").get_text(strip=True)
        author = quote_div.select_one(".author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_div.select(".tags .tag")]
        quotes.append(Quote(text=text, author=author, tags=tags))
    return quotes


def get_all_quotes():
    quotes = []
    next_page = "/"
    while next_page:
        url = urljoin(BASE_URL, next_page)
        soup = get_soup(url)
        quotes.extend(parse_quotes_from_page(soup))
        next_button = soup.select_one(".pager .next a")
        next_page = next_button['href'] if next_button else None
    return quotes


def write_quotes_to_csv(quotes, output_csv_path):
    with open(output_csv_path, mode="w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text", "Author", "Tags"])
        for quote in quotes:
            writer.writerow([quote.text, quote.author, ", ".join(quote.tags)])


def main(output_csv_path):
    quotes = get_all_quotes()
    write_quotes_to_csv(quotes, output_csv_path)
