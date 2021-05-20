from dataclasses import dataclass
import requests

from website_crawler.parser import WebPage, Parser


@dataclass
class Scraper:

    parser: Parser

    def get_page(self, url: str) -> WebPage:
        response = requests.get(url)
        # parser = Parser()
        return self.parser.parse(response.text, url)