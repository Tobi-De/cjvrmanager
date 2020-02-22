from collections import Iterable

from .models import Testimony, Plaintiff, Victim


def depositions_get_by_plaintiff(*, fetched_by: Plaintiff) -> Iterable[Plaintiff]:
    testimonies = Testimony.objects.all()
    p_testimonies = []
    for testimony in testimonies:
        if testimony.plaintiff == fetched_by:
            p_testimonies.append(testimony)
    return p_testimonies


def depositions_get_by_victim(*, fetched_by: Victim) -> Iterable[Victim]:
    testimonies = Testimony.objects.all()
    p_testimonies = []
    for testimony in testimonies:
        if testimony.victim == fetched_by:
            p_testimonies.append(testimony)
    return p_testimonies
