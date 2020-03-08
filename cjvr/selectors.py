import json

from django.db.models import Value
from django.db.models.functions import Concat

from .models import Testimony, Victim, AggressionType, Plaintiff, Report
from .utils import calculate_stat


def person_search(search, model):
    """Create a new colum full_name using concat and filter though this new column"""
    return model.objects.annotate(full_name=Concat("first_name", Value(" "), "last_name")).filter(
        full_name__icontains=search)


def depositions_get_by_plaintiff(*, plaintiff: Plaintiff):
    """get all deposition and return the one report by the plaintiff"""
    return Testimony.objects.select_related("plaintiff").filter(plaintiff=plaintiff)


def depositions_get_by_victim(*, victim: Victim):
    """get all deposition and return the one related to the victim"""
    return Testimony.objects.select_related('victim').filter(victim=victim)


def get_statistics():
    """return statistics based on the number of registered aggressions for all types of aggressions"""
    victims = Victim.objects.prefetch_related('aggressions').all()
    victims_nbr = victims.count()

    # this is the dictionary that is gonna be send to the view
    stats = {
        "amputation": 0,
        "assassinat": 0,
        "viol": 0,
        "flagellation": 0,
        "destruction de patrimoine culturel": 0,
        "atteinte à l’intégrité physique": 0,
        "maltraitance psychologique": 0,
        "destruction et extorsion de biens": 0,
    }

    # we have 8 aggression type, for each of them we calculate the stat of the number of aggression that was
    # registered for the type we are on, range(1, 9) => 1, 2,....8
    template_graphics = dict()
    with open("jsonGraphics/graphics.json", "r") as template:
        template_graphics = json.loads(template.read())

    template.close()
    i = 1
    for stat in stats.keys():
        stats[stat] = calculate_stat(victims.filter(
            aggressions=AggressionType.objects.get(id=i)).count(), victims_nbr)
        if len(template_graphics["datasets"][0]["data"]) >= 8:
            template_graphics["datasets"][0]["data"].clear()
        template_graphics["datasets"][0]["data"].append(str(stats[stat]))
        i += 1

    graphics_final_json = json.dumps(template_graphics, indent=4)
    with open("jsonGraphics/graphics.json", "w") as template:
        template.write(graphics_final_json)
        template.close()

    # here
    with open("cjvr/static/cjvr/graphics.json", "w") as template:
        template.write(graphics_final_json)
    return stats


def report_by_testimony(*, testimony: Testimony):
    return Report.objects.select_related("testimony").filter(testimony=testimony)