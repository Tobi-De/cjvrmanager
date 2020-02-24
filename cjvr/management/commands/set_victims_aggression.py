import os

from django.core.management.base import BaseCommand, CommandError

from cjvr.models import Victim, AggressionType
from .utils import generateIntervalle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class Command(BaseCommand):
    help = "Populate database with fake aggressions for all victims"

    def handle(self, *args, **options):
        try:
            victims = Victim.objects.all()
            for victim in victims:
                list = generateIntervalle()
                Victim.objects.get(id=victim.id).aggressions.set(
                    AggressionType.objects.filter(id__gte=list[0], id__lte=list[1]))
            print("Victims aggressions add")
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
