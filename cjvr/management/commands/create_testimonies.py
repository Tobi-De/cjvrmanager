import json
import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


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
            """
                code goes here
                Ici c'est un peu plus compliquer, tu dois parcouris la base de donnees et recuperer tout les plaintiff et toute les victims
                d'ailleurs, ecrit d'abord le code pour la partie victim, dans le fichier json la, ajoute le meme nombre de plaingnant que de victim, genre 
                5 a chaque fois, tu parcourt les deux objects dans lesquelles tu auras recupere les victim et les plaignant et tu cree les depositions,
                c'est ca testimonies la, et tu y ajoute la description depuis le fichier json, donc ca veut dire que dans le json, la section temoignage la, tu
                ajoute juste 5 description au hasard, bon finalment c'est pas compliquer 
            """
            print("Testimonies add")
        except Exception as e:
            return {e}
