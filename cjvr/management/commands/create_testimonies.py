import json
import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from cjvr.models import Plaintiff
from cjvr.models import Victim
from cjvr.models import Testimony


class Command(BaseCommand):
    help = "Populate database with fake testimonies"

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        try:
            file_path = os.path.join(BASE_DIR, options['file'])
            with open(file_path, 'r') as f:
                json_object = json.load(f)
                Command.add_testimonies(json_object)
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")

    @staticmethod
    def add_testimonies(json_object):
        try:
            plaintiffs = Plaintiff.objects.all()
            victims = Victim.objects.all()
            testimonies = json_object['testimonies']
            for i, testimony in enumerate(testimonies):
                Testimony.objects.create(plaintiff=plaintiffs[i], victim=victims[i],
                                         description=testimony['description'])
            print("Testimonies add")
        except Exception as e:
            print(e)
            return {e}
