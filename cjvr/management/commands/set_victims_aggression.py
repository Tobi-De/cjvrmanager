import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cjvr.management.commands.utils import generateIntervalle
from cjvr.models import Victim, AggressionType


class Command(BaseCommand):
    help = "Populate database with fake aggressions for all victims"

    def handle(self, *args, **options):
        try:
            """
                code goes here 
                bon ici ca pourrait etre compliquer
                tu vas cree dans ce dossier la,le dossier commands, un fichier utils.py, dedans tu cree une fonction ou 
                plusieurs (a toi de voir) qui produit 2 chiffre aleatoire entre 1 et et 8, parce qu'il y a 8 type 
                d'aggressions et ensuite tu parcourt chaque victime, et tu fait un aggressions.set() sur chaque object
                en recuperant au hasard une ou plusieurs aggressions parmis les types d'aggressions enregistre
                pour faire le setAggression tu fais
                Victim.objects.get(id=x).aggressions.set(AggressionType.objects.filter(id__lte=y, id__gte=z))
                le x c'est l'id des victims, y et z c'est un intervalle de valeurs pour les aggressions, parce
                 que le aggressions.set() veut forcement qu'on lui passe un iterable, donc il faut un intervalle,
                 gte == greater than or equal to,
                  lte = less than or equal to
                  au final tu dois generer aleatoirement y et z pour pouvoir affecter des aggressions au victims, y et z 
                  doivent etre compris entre 1 et 8 et y <= z
            """
            victims = Victim.objects.all()
            for victim in victims:
                list = generateIntervalle()
                Victim.objects.get(id=victim.id).aggressions.set(AggressionType.objects.filter(id__lte=list[0], id__gte=list[1]))

            print("Victims aggressions add")
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
