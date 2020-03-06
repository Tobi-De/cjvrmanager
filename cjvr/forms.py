from django import forms

from .models import Victim, Plaintiff, Testimony, Task, Report


class VictimCreationForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = ['first_name', 'last_name', 'age', 'sex', 'religion', 'address', 'aggression_place', 'status',
                  'aggressions']


class PlaintiffCreationForm(forms.ModelForm):
    class Meta:
        model = Plaintiff
        fields = ['first_name', 'last_name', 'age', 'sex', 'religion', 'address', 'contact']


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
        fields = ['name', 'description', 'start_date', 'end_date']

    def clean_end_date(self):
        start = self.cleaned_data.get('start_date')
        end = self.cleaned_data.get('end_date')
        if start > end:
            raise forms.ValidationError("Ceci n'est pas une date de fin valide")
        return end


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50)

