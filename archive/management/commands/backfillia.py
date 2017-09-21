import logging
from django.conf import settings
from archive.models import Screenshot
from internetarchive import upload, get_item, get_files
from django.core.management.base import BaseCommand
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Backload screenshots to the Internet Archive'

    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int, default=5)

    def handle(self, *args, **options):
        obj_list = Screenshot.objects.filter(internetarchive_id='')[:options['count'][0]]
        [obj.sync_with_ia() for obj in obj_list]
