from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import TestimonyCreationForm, PlaintiffCreationForm, VictimCreationForm, ReportCreationForm
from .models import Testimony, Victim, Plaintiff, Report
from .selectors import get_statistics, person_search, report_by_testimony
from .services import plaintiff_create, victim_create, testimony_create


class TestimonyList(ListView):
    model = Testimony
    template_name = 'cjvr/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-register_date']


class TestimonyDetail(DetailView):
    model = Testimony

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['report'] = report_by_testimony(fetched_by=context['testimony'])
        return context


class VictimsList(ListView):
    model = Victim
    template_name = 'cjvr/victims_list.html'
    context_object_name = 'victims'
    ordering = ['-register_date']

    """def get_queryset(self):
        result = super(VictimsList, self).get_queryset()

        query = self.request.GET.get('search')
        if query:
            result = person_search(query, Victim)
        return result"""


class VictimDetail(DetailView):
    model = Victim


class PlaintiffsList(ListView):
    model = Plaintiff
    template_name = 'cjvr/plaintiffs_list.html'
    context_object_name = 'plaintiffs'
    ordering = ['-register_date']

    """def get_queryset(self):
        result = super(PlaintiffsList, self).get_queryset()

        query = self.request.GET.get('search')
        if query:
            result = person_search(query, Plaintiff)
        return result"""


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
            return redirect('testimonies')
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
    if request.method == "POST":
        report_form = ReportCreationForm(request.POST)
        if report_form.is_valid():
            Report.objects.create(testimony=Testimony.objects.get(id=testimony_id),
                                  content=report_form.cleaned_data['content'])
            return redirect('testimony-detail', testimony_id)
    else:
        report_form = ReportCreationForm()
    context = {
        "report_form": report_form
    }
    return render(request, 'cjvr/register_report.html', context)


def detail_report(request, testimony_id):
    pass


def register_task(request):
    pass


def detail_task(request):
    pass


def statistics_graph(request):
    return render(request, 'cjvr/statistics_graph.html', {"stats": get_statistics()})


def search_result(request):
    victims = person_search(request.GET.get('q'), Victim)
    plaintiffs = person_search(request.GET.get('q'), Plaintiff)
    context = {
        'victims': victims,
        'plaintiffs': plaintiffs
    }
    return render(request, "cjvr/search_result.html", context)


def delete_plaintiff(request, plaintiff_id):
    if request.method == "POST":
        Plaintiff.objects.get(id=plaintiff_id).delete()
        return redirect('plaintiffs')
    return render(request, 'cjvr/confirm_sup_plaintiff.html', {'plaintiff': Plaintiff.objects.get(id=plaintiff_id)})


def delete_testimony(request, testimony_id):
    if request.method == "POST":
        Testimony.objects.get(id=testimony_id).delete()
        return redirect('testimonies')
    return render(request, 'cjvr/confirm_sup_testimony.html', {'testimony': Testimony.objects.get(id=testimony_id)})


def delete_victim(request, victim_id):
    if request.method == "POST":
        Victim.objects.get(id=victim_id).delete()
        return redirect('victims')
    return render(request, 'cjvr/confirm_sup_victim.html', {'victim': Victim.objects.get(id=victim_id)})
