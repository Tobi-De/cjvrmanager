import json
import os

from django.core.management.base import BaseCommand, CommandError

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
            """
                code goes here
                bon ici c'est la meme chose que plaignant, et l'attribut pour TypeAgression la zape ca, c'est le dernier fichier qui s'en occupe
                donc tu parcourt et tu cree 5 victim, vas voir les models pour comprendre mieux comment cree les objets
            """
            print("Victims add")
        except Exception as e:
            return {e}
