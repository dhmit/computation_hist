from django.core.management.base import BaseCommand

from utilities.metadata_parser import populate_from_metadata

class Command(BaseCommand):
    def handle(self, *args, **options):
        populate_from_metadata()
