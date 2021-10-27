from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from recruitment.models import Job

class JobForm(forms.ModelForm):
    branches_allowed = SimpleArrayField(forms.CharField(max_length=10))
    class Meta:
        model = Job
        fields = '__all__'