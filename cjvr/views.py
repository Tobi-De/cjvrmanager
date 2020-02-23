from django.shortcuts import render

from .forms import (TestimonyCreationForm, VictimCreationForm, PlaintiffCreationForm)


def home(request):
    if request.method == "POST":
        t_form = TestimonyCreationForm(request.POST)
        v_form = VictimCreationForm(request.POST)
        p_form = PlaintiffCreationForm(request.POST)
        if t_form.is_valid() and v_form.is_valid() and p_form.is_valid():
            pass
    else:
        t_form = TestimonyCreationForm()
        v_form = VictimCreationForm()
        p_form = PlaintiffCreationForm()
    context = {
        "p_form": p_form,
        "t_form": t_form,
        "v_form": v_form
    }
    return render(request, 'cjvr/index.html', context)
