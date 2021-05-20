import requests

from website_crawler.parser import WebPage, Parser


class Scraper:

    def get_page(self, url: str) -> WebPage:
        response = requests.get(url)
        parser = Parser()
        return parser.parse(response.text, url)
