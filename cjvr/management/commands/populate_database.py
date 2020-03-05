import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Populate database the first time with all the datas"

    def handle(self, *args, **options):
        try:
            os.system("python manage.py create_aggressions fakedata.json")
            os.system("python manage.py create_victims fakedata.json")
            os.system("python manage.py create_plaintiffs fakedata.json")
            os.system("python manage.py set_victims_aggression")
            os.system("python manage.py create_testimonies fakedata.json")
        except Exception as e:
            raise CommandError(f"Something went wrong: {e}")
