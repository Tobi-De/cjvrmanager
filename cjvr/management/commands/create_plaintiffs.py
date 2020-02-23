import json
import os

from django.core.management.base import BaseCommand, CommandError

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
            """
                code goes here
                loop over all object in the json_object (inspire toi de create_aggressions qui marche deja)
                create plaintiff for each one (normalement je devais ajouter des plaignant dans le fichier fakedata.json mais c'est pas encore fait, si tu
                regarde dans le fichier, c'est a la base du projet tu sauras comment remplir ca)
            """
            print("Plaintiffs add")
        except Exception as e:
            return {e}
