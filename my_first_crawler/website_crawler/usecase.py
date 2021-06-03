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
        return

    # TODO: urlがクロール済みかどうか判定 早期リターン
    if url in [w.url for w in crawled_pages]:
        return

    # TODO: scrapeする title and description
    scraper = Scraper(Parser())
    web_page = scraper.get_page(url)
    crawled_pages.append(web_page)

    for link in web_page.link_list:
        crawl(link, seed_domain)


# def crawl_web_page_links(web_page: WebPage, seed_domain: str) -> List[WebPage]:
#     scraper = Scraper(Parser())
#     web_page_list = []
#
#     # TODO: 同じドメイン、クロール済みだったらスキップする
#     # クロールずみの WebPage なら link_list を見なくてもいいよね
#
#     for link in web_page.link_list:
#         link_domain = urlparse(link).netloc
#
#         # 同じドメインの URL だったら scrapeする、違ったらスキップする (外に出ていかなようにする)
#         if link_domain != seed_domain:
#             print('skip_url:', link)
#             continue
#
#         if link in crawled_url:
#             print('skip_url:', link)
#             continue
#
#         web_page_list.append(scraper.get_page(link))
#         crawled_url.append(link)
#         # TODO: scraper.get_page(link) に対して crawl_web_page_links を呼ぶ
#
#     return web_page_list
