
from website_crawler.usecase import start

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('seed_url', type=str)
        pass

    def handle(self, seed_url, **options):
        print(seed_url)
        start(seed_url)
