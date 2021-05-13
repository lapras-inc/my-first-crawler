from unittest import TestCase

from website_crawler.parser import Parser


class TestParser(TestCase):
    def test(self):
        parser = Parser()

        result = parser.parse(
            '<html><head><title>LAPRASモブプロ</title><description>生配信スタート</description></head><body></body><html>'
        )

        self.assertEqual(result, {
            "title": "LAPRASモブプロ",
            "description": "生配信スタート"
        })