from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from recruitment.models import Job,JobRound

class JobForm(forms.ModelForm):
    branches_allowed = SimpleArrayField(forms.CharField(max_length=10))
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['applied_by', 'num_of_students_applied']

class JobRoundForm(forms.ModelForm):
    class Meta:
        model = JobRound
        fields = '__all__'