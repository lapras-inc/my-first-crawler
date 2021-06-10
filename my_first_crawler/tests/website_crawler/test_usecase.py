from unittest import TestCase
from unittest.mock import Mock

from website_crawler.parser import WebPage
from website_crawler.scraper import Scraper
from website_crawler.usecase import CrawlUsecase


class TestCrawl(TestCase):
    def test_start(self):
        scraper = Mock(spec=Scraper)
        data = {
            'https://test.lapras.com': WebPage(title='', description='', link_list=[
                'https://test.lapras.com/1',
                'https://test.lapras.com/2',
                'https://zettai-dame.lapras.com/2',
            ]),
            'https://test.lapras.com/1': WebPage(title='', description='', link_list=[
                'https://test.lapras.com/1-2'
            ]),
            'https://test.lapras.com/1-2': WebPage(title='', description='', link_list=[
                'https://test.lapras.com/1'
            ]),
            'https://test.lapras.com/2': WebPage(title='', description='', link_list=[]),
        }
        scraper.get_page.side_effect = lambda url: data[url]

        seed_url = 'https://test.lapras.com'
        usecase = CrawlUsecase(scraper)
        result = usecase.start(seed_url)

        self.assertEqual(len(result), 4)
        self.assertEqual({r['url'] for r in result}, {
            'https://test.lapras.com',
            'https://test.lapras.com/1',
            'https://test.lapras.com/2',
            'https://test.lapras.com/1-2',
        })
