from unittest import TestCase, mock

import responses
from website_crawler.scraper import Scraper
from website_crawler.parser import Parser


class TestScraper(TestCase):
    @responses.activate
    def test(self):

        html = '''
        <html>
            <head>
              <title>LAPRASモブプロ</title>
              <meta name="description" content="生配信スタート"></meta>
            </head>
            <body>
              <a href="https://lapras.com">LAPRAS</a>
              <a href="hoge/fuga">LAPRAS</a>
              <a href="//example.com">LAPRAS</a>
            </body>
        </html>
        '''

        url = "https://lapras.com"
        responses.add(responses.GET, url,
                  body=html, status=200)
        mock_parser = mock.Mock(spec=Parser)

        scraper = Scraper(parser=mock_parser)
        print(scraper.get_page(url))

        mock_parser.parse.assert_called_once()

        pass
