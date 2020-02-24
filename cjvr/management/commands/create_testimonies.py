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
            """
                code goes here
                Ici c'est un peu plus compliquer, tu dois parcouris la base de donnees et recuperer tout les plaintiff 
                et toute les victims d'ailleurs, ecrit d'abord le codplaintiffe pour la partie victim, dans le fichier json la,
                ajoute le meme nombre de plaignant que de victim, genre 10 a chaque fois, tu parcourt les deux objects
                dans lesquelles tu recupere les victimes et les plaignants et tu cree les depositions,
                c'est ca testimonies la, et tu y ajoute la description depuis le fichier json, donc ca veut dire que 
                dans le json, la section temoignage la, tu
                ajoute juste 10 description au hasard, bon finalment c'est pas compliquer, pour les descriptions la faut 
                que sa parle de violence sans etre trop precis,
                la on pourra ajouter n'importe quel type d'aggressions au victime et ca restera coherent 
            """
            plaintiffs = Plaintiff.objects.all()
            victims = Victim.objects.all()
            testimonies = json_object['testimonies']

            i=0
            for testimony in testimonies :
                Testimony.objects.create(plaintiff=plaintiffs[i], victim=victims[i], description=testimony['description'])
                i=i+1
            print("Testimonies add")
        except Exception as e:
            print(e)
            return {e}
