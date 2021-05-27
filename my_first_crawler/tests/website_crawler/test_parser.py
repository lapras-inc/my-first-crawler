from unittest import TestCase

from website_crawler.parser import Parser


class TestParser(TestCase):
    def test(self):
        parser = Parser()

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
        result = parser.parse(html, 'https://test.lapras.com')

        self.assertEqual(result.title, 'LAPRASモブプロ')
        self.assertEqual(result.description, '生配信スタート')
        self.assertIn('https://lapras.com', result.link_list)
        self.assertIn('https://test.lapras.com/hoge/fuga', result.link_list)
        self.assertIn('https://example.com', result.link_list)

    def test_no_description(self):
        parser = Parser()

        html = '''
        <html>
            <head>
              <title>LAPRASモブプロ</title>
            </head>
            <body>
              <a href="https://lapras.com">LAPRAS</a>
              <a href="hoge/fuga">LAPRAS</a>
              <a href="//example.com">LAPRAS</a>
            </body>
        </html>
        '''
        result = parser.parse(html, 'https://test.lapras.com')

        self.assertEqual(result.title, 'LAPRASモブプロ')
        self.assertIsNone(result.description)
