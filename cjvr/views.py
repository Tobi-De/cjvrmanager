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


def testimony_list(request):
    pass


def testimony_detail(request, testimony_id):
    pass


def victims_list(request):
    pass


def victim_detail(request):
    pass


def plaintiffs_list(request):
    pass


def plaintiff_detail(request):
    pass


def register_testimony(request):
    pass


def register_report(request, testimony_id):
    pass


def report_detail(request, testimony_id):
    pass


def statistics_graph(request):
    pass
