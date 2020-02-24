import json
import os

from django.core.management.base import BaseCommand, CommandError

from cjvr.models import Victim

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with fake victims"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        try:
            file_path = os.path.join(BASE_DIR, options['file'])
            with open(file_path, 'r') as f:
                json_object = json.load(f)
                Command.add_victims(json_object)
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")

    @staticmethod
    def add_victims(json_object):
        try:
            victims = json_object['victims']
            for victim in victims:
                Victim.objects.create(first_name=victim['first_name'], last_name=victim['last_name'],
                                      age=victim['age'], sex=victim['sex'], religion=victim['religion'],
                                      address=victim['address'], aggression_place=victim['aggression_place'],
                                      status=victim['status'])
            print("victims add")
        except Exception as e:
            print(e)
            return {e}
