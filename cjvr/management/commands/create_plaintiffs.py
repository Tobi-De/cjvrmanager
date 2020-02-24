import json
import os

from django.core.management.base import BaseCommand, CommandError

from cjvr.models import Plaintiff

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with fake plaintiffs"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        try:
            file_path = os.path.join(BASE_DIR, options['file'])
            with open(file_path, 'r') as f:
                json_object = json.load(f)
                Command.add_plaintiffs(json_object)
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")

    @staticmethod
    def add_plaintiffs(json_object):
        # add plaintiff to database from json file
        try:
            plaintiffs = json_object['Plaintiffs']
            for plaintiff in plaintiffs:
                Plaintiff.objects.create(first_name=plaintiff['first_name'], last_name=plaintiff['last_name'],
                                         age=plaintiff['age'], sex=plaintiff['sex'], religion=plaintiff['religion'],
                                         address=plaintiff['address'], contact=plaintiff['contact'])
            print("Plaintiffs add")
        except Exception as e:
            print(e)
            return {e}
