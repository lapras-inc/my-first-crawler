from typing import List
from urllib.parse import urlparse

from website_crawler.parser import Parser, WebPage
from website_crawler.scraper import Scraper

crawled_url: List[str] = []
crawled_pages: List[object] = []


def start(seed_url: str):
    # TODO: seed_url を scrape する
    # TODO: オンメモリで scrape した URL をクロール済みの URL を持っておく
    # TODO: 戻りの WebPage.link_list の URL を再帰的に scrape する
    # TODO: クロール対象の URL がすでにクロール済みだったらスキップする
    # TODO: 同じドメインの URL だったら scrapeする、違ったらスキップする (外に出ていかなようにする)
    seed_domain = urlparse(seed_url).netloc
    crawl(seed_url, seed_domain)
    print(crawled_pages)


def crawl(url, seed_domain):
    # TODO: urlがhostのURLに属するか判定 早期リターン
    if urlparse(url).netloc != seed_domain:
        print('skip-しらんドメイン:', url)
        return

    # TODO: urlがクロール済みかどうか判定 早期リターン
    if url in [w['url'] for w in crawled_pages]:
        print('skip-クロールずみ:', url)
        return

    if is_dame(url):
        return


    # TODO: scrapeする title and description
    scraper = Scraper(Parser())
    web_page = scraper.get_page(url)
    crawled_pages.append({'url': url, 'web_page': web_page })

    for link in web_page.link_list:
        crawl(link, seed_domain)


def is_dame(url: str) -> bool:
    return False
    # if re.sarch(r'.mp4$', url):
    #     print('mp4だよ', url)
