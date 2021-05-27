from website_crawler.parser import Parser
from website_crawler.scraper import Scraper


def crawl(seed_url: str):
    # TODO: seed_url を scrape する
    # TODO: オンメモリで scrape した URL をクロール済みの URL を持っておく
    # TODO: 戻りの WebPage.link_list の URL を再帰的に scrape する
    # TODO: クロール対象の URL がすでにクロール済みだったらスキップする
    # TODO: 同じドメインの URL だったら scrapeする、違ったらスキップする (外に出ていかなようにする)
    crawled_url = []
    scraper = Scraper(Parser())
    web_page = scraper.get_page(seed_url)
    crawled_url.append(seed_url)
    print(web_page)

    for link in web_page.link_list:
        if link in crawled_url:
            continue
        print('get_page', link)
        web_page = scraper.get_page(link)
        crawled_url.append(link)
        print(web_page)
