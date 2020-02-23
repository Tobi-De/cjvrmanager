import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with fake aggressions for all victims"

    def handle(self, *args, **options):
        try:
            # code goes here
            pass
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
