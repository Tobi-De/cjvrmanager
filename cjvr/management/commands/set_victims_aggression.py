import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with fake aggressions for all victims"

    def handle(self, *args, **options):
        try:
            """
                code goes here 
                bon ici ca pourrait etre compliquer
                tu vas cree dans ce dossier la,le dossier command, un fichier utils.py, dedans tu cree une fonction
                qui en fonction produit une serie de chiffre aleatoire entre 0 et et 7, parce qu'il y a 8 type d'aggressions
                et ensuite tu parcourt chaque victime, et tu fait un setAggression() sur chaque object en recuperant au hasard une aggressions dans les objets
                aggressions enregistre, au pire tu recupere les 5 premier aggression, tu vas trouver
                pour faire le setAggression tu fais
                Victim.objects.get(id=x).setAggression(AggressionType.objects.get(id=y)
                le x c'est l'id des victims, y l'id des aggressions, tu vas trouver, ecrit moi si t'a un soucis
            """
            pass
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
