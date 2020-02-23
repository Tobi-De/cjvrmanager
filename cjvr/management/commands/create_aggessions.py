import json
import os

from django.core.management.base import BaseCommand, CommandError

from cjvr.models import AggressionType

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with aggressions type"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        try:
            file_path = os.path.join(BASE_DIR, options['file'])
            with open(file_path, 'r') as f:
                json_object = json.load(f)
                Command.add_aggressions(json_object)
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")

    @staticmethod
    def add_aggressions(json_object):
        try:
            aggressions = json_object['aggressions']
            for aggression in aggressions:
                AggressionType.objects.create(name=aggression['name'], description=aggression['description'])
            print("Aggressions add")
        except Exception as e:
            return {e}
