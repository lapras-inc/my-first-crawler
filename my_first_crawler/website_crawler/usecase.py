from typing import List
from urllib.parse import urlparse

from website_crawler.parser import Parser, WebPage
from website_crawler.scraper import Scraper


class CrawlUsecase:
    crawled_url: List[str] = []
    crawled_pages: List[object] = []

    def __init__(self, scraper: Scraper):
        self.scraper = scraper

    def start(self, seed_url: str) -> List[object]:
        # TODO: seed_url を scrape する
        # TODO: オンメモリで scrape した URL をクロール済みの URL を持っておく
        # TODO: 戻りの WebPage.link_list の URL を再帰的に scrape する
        # TODO: クロール対象の URL がすでにクロール済みだったらスキップする
        # TODO: 同じドメインの URL だったら scrapeする、違ったらスキップする (外に出ていかなようにする)
        seed_domain = urlparse(seed_url).netloc
        self.crawl(seed_url, seed_domain)
        print(self.crawled_pages)
        return self.crawled_pages

    def crawl(self, url, seed_domain):
        # TODO: urlがhostのURLに属するか判定 早期リターン
        if urlparse(url).netloc != seed_domain:
            print('skip-しらんドメイン:', url)
            return

        # TODO: urlがクロール済みかどうか判定 早期リターン
        if url in [w['url'] for w in self.crawled_pages]:
            print('skip-クロールずみ:', url)
            return

        # TODO: scrapeする title and description
        # scraper = Scraper(Parser())
        web_page = self.scraper.get_page(url)
        self.crawled_pages.append({'url': url, 'web_page': web_page})

        for link in web_page.link_list:
            self.crawl(link, seed_domain)
