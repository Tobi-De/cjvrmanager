from .models import Testimony, Plaintiff, Victim, AggressionType

SOUDAN_POPULATION = 40_530_000


def depositions_get_by_plaintiff(*, fetched_by: Plaintiff):
    """get all deposition and return the one report by the plaintiff"""
    testimonies = Testimony.objects.select_related('plaintiff').all()
    p_testimonies = []
    for testimony in testimonies:
        if testimony.plaintiff == fetched_by:
            p_testimonies.append(testimony)
    return p_testimonies


def depositions_get_by_victim(*, fetched_by: Victim):
    """get all deposition and return the one related to the victim"""
    testimonies = Testimony.objects.select_related('victim').all()
    p_testimonies = []
    for testimony in testimonies:
        if testimony.victim == fetched_by:
            p_testimonies.append(testimony)
    return p_testimonies


def get_statistics():
    """return statistics based on the number of registered aggressions for all types of aggressions"""
    victims = Victim.objects.prefetch_related('aggressions').all()

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
    for i in range(1, 9):
        for stat in stats:
            stats[stat] = calculate_stat(victims.filter(aggressions=AggressionType.objects.get(id=i)).count())

    return stats


def calculate_stat(aggression_nbr):
    """this is not a selector"""
    return (aggression_nbr * 100) / SOUDAN_POPULATION
