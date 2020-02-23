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
    aggressions = AggressionType.objects.all()

    """for aggression in aggressions:
        nb = victims.filter(aggressions)"""


def calculate_stat(aggression_nbr):
    """this is not a selector"""
    return (aggression_nbr * 100) / SOUDAN_POPULATION
