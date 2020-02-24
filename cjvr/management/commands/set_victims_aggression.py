import os

from django.core.management.base import BaseCommand, CommandError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cjvr.management.commands.utils import generateIntervalle
from cjvr.models import Victim, AggressionType


class Command(BaseCommand):
    help = "Populate database with fake aggressions for all victims"

    def handle(self, *args, **options):
        try:
            victims = Victim.objects.all()
            for victim in victims:
                list = generateIntervalle()
                Victim.objects.get(id=victim.id).aggressions.set(
                    AggressionType.objects.filter(id__lte=list[0], id__gte=list[1]))

            print("Victims aggressions add")
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
