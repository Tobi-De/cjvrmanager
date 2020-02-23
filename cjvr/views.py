from django.shortcuts import render

from .models import Plaintiff
from .selectors import depositions_get_by_plaintiff


def home(request):
    plaintiffs = depositions_get_by_plaintiff(fetched_by=Plaintiff.objects.first())
    return render(request, 'cjvr/index.html', {'plaintiffs': plaintiffs})
