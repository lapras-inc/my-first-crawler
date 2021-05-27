from dataclasses import dataclass
from typing import List, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup


@dataclass(frozen=True)
class WebPage:
    title: str
    description: Optional[str]
    # ページ内に含まれるリンクURL
    link_list: List[str]


class Parser:

    def parse(self, html: str, base_url: str) -> WebPage:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('title').get_text()
        description_elem = soup.select_one('meta[name="description"]')
        link_list = [urljoin(base_url, a['href']) for a in soup.select('a')]

        return WebPage(
            title=title,
            description=description_elem['content'] if description_elem else None,
            link_list=link_list,
        )
