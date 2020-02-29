from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, DeleteView

from .forms import TestimonyCreationForm, PlaintiffCreationForm, VictimCreationForm, ReportCreationForm, \
    TaskCreationForm
from .models import Testimony, Victim, Plaintiff, Report, Task
from .selectors import get_statistics, person_search, report_by_testimony
from .services import plaintiff_create, victim_create, testimony_create


class TestimonyList(LoginRequiredMixin, ListView):
    model = Testimony
    template_name = 'cjvr/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-register_date']
    paginate_by = 5


class TestimonyDetail(LoginRequiredMixin, DetailView):
    model = Testimony

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['report'] = report_by_testimony(fetched_by=context['testimony'])
        return context


class VictimsList(LoginRequiredMixin, ListView):
    model = Victim
    template_name = 'cjvr/victims_list.html'
    context_object_name = 'victims'
    ordering = ['-register_date']
    paginate_by = 5


class VictimDetail(LoginRequiredMixin, DetailView):
    model = Victim


class PlaintiffsList(LoginRequiredMixin, ListView):
    model = Plaintiff
    template_name = 'cjvr/plaintiffs_list.html'
    context_object_name = 'plaintiffs'
    ordering = ['-register_date']
    paginate_by = 5


class PlaintiffDetail(LoginRequiredMixin, DetailView):
    model = Plaintiff


@login_required
def add_plaintiff(request):
    if request.method == "POST":
        p_form = PlaintiffCreationForm(request.POST)
        if p_form.is_valid():
            plaintiff = plaintiff_create(p_form)
            messages.success(request, "Plaignant cree avec succes")
            return redirect('add-victim', plaintiff.id)
    else:
        p_form = PlaintiffCreationForm()
    return render(request, "cjvr/add_plaintiff.html", {"p_form": p_form})


@login_required
def add_victim(request, pl_id):
    if request.method == "POST":
        v_form = VictimCreationForm(request.POST)
        if v_form.is_valid():
            victim = victim_create(v_form)
            messages.success(request, "Victime cree avec succes")
            return redirect('register-testimony', pl_id, victim.id)
    else:
        v_form = VictimCreationForm()
    return render(request, "cjvr/add_victim.html", {"v_form": v_form})


@login_required
def register_testimony(request, pl_id, vic_id):
    if request.method == "POST":
        t_form = TestimonyCreationForm(request.POST)
        if t_form.is_valid():
            plaintiff = Plaintiff.objects.get(id=pl_id)
            victim = Victim.objects.get(id=vic_id)
            testimony_create(plaintiff, victim, t_form.cleaned_data['description'])
            messages.success(request, "Deposition cree avec succes")
            return redirect('testimonies')
    else:
        t_form = TestimonyCreationForm()
    context = {
        "t_form": t_form,
    }
    return render(request, 'cjvr/register_testimony.html', context)


@login_required
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
        "report_form": report_form,
        "testimony_id": testimony_id
    }
    return render(request, 'cjvr/register_report.html', context)


@login_required
def register_task(request):
    if request.method == "POST":
        task_form = TaskCreationForm(request.POST)
        if task_form.is_valid():
            if task_form.cleaned_data['end_date'] < task_form.cleaned_data['start_date']:
                messages.info(request, "Votre date de fin ne peut pas etre avant votre date de debut")
                return redirect('register-task')
            else:
                Task.objects.create(user=request.user, name=task_form.cleaned_data['name'],
                                    description=task_form.cleaned_data['description'],
                                    start_date=task_form.cleaned_data['start_date'],
                                    end_date=task_form.cleaned_data['end_date'])
                messages.success(request, "Tache cree avec succes")
                return redirect('task-list')
    else:
        task_form = TaskCreationForm(initial={"start_date": timezone.now()})
    context = {
        "task_form": task_form
    }
    return render(request, 'cjvr/register_task.html', context)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'cjvr/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-register_date']

    def get_queryset(self):
        return Task.objects.all()


class TaskDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    success_url = '/cjvr/tasks'
    template_name = "cjvr/confirm_sup_task.html"

    def test_func(self):
        task = self.get_object()
        return self.request.user == task.user


@login_required
def statistics_graph(request):
    return render(request, 'cjvr/statistics_graph.html', {"stats": get_statistics()})


@login_required
def search_result(request):
    victims = person_search(request.GET.get('q'), Victim)
    plaintiffs = person_search(request.GET.get('q'), Plaintiff)
    context = {
        'victims': victims,
        'plaintiffs': plaintiffs
    }
    return render(request, "cjvr/search_result.html", context)


@login_required
def delete_plaintiff(request, plaintiff_id):
    if request.method == "POST":
        Plaintiff.objects.get(id=plaintiff_id).delete()
        messages.success(request, "Plaignant supprimer avec succes")
        return redirect('plaintiffs')
    return render(request, 'cjvr/confirm_sup_plaintiff.html', {'plaintiff': Plaintiff.objects.get(id=plaintiff_id)})


@login_required
def delete_testimony(request, testimony_id):
    if request.method == "POST":
        Testimony.objects.get(id=testimony_id).delete()
        messages.success(request, "Deposition supprime avec succes")
        return redirect('testimonies')
    return render(request, 'cjvr/confirm_sup_testimony.html', {'testimony': Testimony.objects.get(id=testimony_id)})


@login_required
def delete_victim(request, victim_id):
    if request.method == "POST":
        Victim.objects.get(id=victim_id).delete()
        return redirect('victims')
    return render(request, 'cjvr/confirm_sup_victim.html', {'victim': Victim.objects.get(id=victim_id)})


@login_required
def add_testimony(request, type, pk):
    if request.method == "POST":
        t_form = TestimonyCreationForm(request.POST)
        if type == "plaintiff":
            form = VictimCreationForm(request.POST)
            if form.is_valid() and t_form.is_valid():
                plaintiff = Plaintiff.objects.get(id=pk)
                victim = victim_create(form)
                testimony_create(plaintiff, victim, t_form.cleaned_data['description'])
                messages.success(request, "Deposition cree avec succes")
                return redirect('testimonies')
        else:
            form = PlaintiffCreationForm(request.POST)
            if form.is_valid() and t_form.is_valid():
                victim = Victim.objects.get(id=pk)
                plaintiff = plaintiff_create(form)
                testimony_create(plaintiff, victim, t_form.cleaned_data['description'])
                messages.success(request, "Deposition cree avec succes")
                return redirect('testimonies')
    else:
        t_form = TestimonyCreationForm()
        if type == "plaintiff":
            form = VictimCreationForm()
        else:
            form = PlaintiffCreationForm()
    context = {
        "t_form": t_form,
        "form": form,
        "type": type
    }
    return render(request, 'cjvr/add_testimony.html', context)
