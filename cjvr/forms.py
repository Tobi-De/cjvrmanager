from django import forms

from .models import Victim, Plaintiff, Testimony, Task, Report


class VictimCreationForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['first_name', 'last_name', 'age', 'sexe', 'religion', 'address', 'aggression_place', 'status',
                  'aggressions']


class PlaintiffCreationForm(forms.ModelForm):
    class Meta:
        model = Plaintiff
        fields = ['first_name', 'last_name', 'age', 'sexe', 'religion', 'address', 'contact']


class TestimonyCreationForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['description']


class ReportCreationForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['content']


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description']
