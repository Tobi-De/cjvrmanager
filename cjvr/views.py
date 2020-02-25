from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import TestimonyCreationForm, PlaintiffCreationForm, VictimCreationForm
from .models import Testimony, Victim, Plaintiff
from .selectors import get_statistics
from .services import plaintiff_create, victim_create, testimony_create
from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView
import json

def home(request):
    return render(request, 'cjvr/index.html')


class TestimonyList(ListView):
    model = Testimony
    template_name = 'cjvr/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-register_date']


class TestimonyDetail(DetailView):
    model = Testimony


class VictimsList(ListView):
    model = Victim
    template_name = 'cjvr/victims_list.html'
    context_object_name = 'victims'
    ordering = ['-register_date']


class VictimDetail(DetailView):
    model = Victim


class PlaintiffsList(ListView):
    model = Plaintiff
    template_name = 'cjvr/plaintiffs_list.html'
    context_object_name = 'plaintiffs'
    ordering = ['-register_date']


class PlaintiffDetail(DetailView):
    model = Plaintiff


def register_testimony(request):
    if request.method == "POST":
        t_form = TestimonyCreationForm(request.POST)
        v_form = VictimCreationForm(request.POST)
        p_form = PlaintiffCreationForm(request.POST)
        if t_form.is_valid() and v_form.is_valid() and p_form.is_valid():
            plaintiff = plaintiff_create(p_form)
            victim = victim_create(v_form)
            testimony_create(plaintiff, victim, t_form.cleaned_data['description'])
            return redirect('home')
    else:
        t_form = TestimonyCreationForm()
        v_form = VictimCreationForm()
        p_form = PlaintiffCreationForm()
    context = {
        "p_form": p_form,
        "t_form": t_form,
        "v_form": v_form
    }
    return render(request, 'cjvr/register_testimony.html', context)


def register_report(request, testimony_id):
    pass


def report_detail(request, testimony_id):
    pass


def register_task(request):
    pass


def report_task(request):
    pass


def statistics_graph(request):
    return render(request, 'cjvr/statistics_graph.html', {"stats": get_statistics()})

def graph(request):
    with open("jsonGraphics/graphics.json", "r") as template:
        data = template.read()
    return JsonResponse(data)

