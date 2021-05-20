from dataclasses import dataclass
from typing import List

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class WebPage:
    title: str
    description: str
    # ページ内に含まれるリンクURL
    link_list: List[str]


class Parser:

    def parse(self, html: str) -> WebPage:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('title').get_text()
        description = soup.select_one('meta[name="description"]')['content']
        link_list = [a['href'] for a in soup.select('a')]

        return WebPage(
            title=title,
            description=description,
            link_list=link_list,
        )
