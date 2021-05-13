from bs4 import BeautifulSoup

class Parser:

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('title').get_text()
        description = soup.select_one('description').get_text()

        return {
            "title": title,
            "description": description
        }