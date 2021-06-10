from website_crawler.parser import Parser
from website_crawler.scraper import Scraper
from website_crawler.usecase import CrawlUsecase

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('seed_url', type=str)
        pass

    def handle(self, seed_url, **options):
        print(seed_url)
        usecase = CrawlUsecase(Scraper(Parser()))
        result = usecase.start(seed_url)
        print(result)
