from django import forms
from django.contrib.postgres.forms import SimpleArrayField

<<<<<<< HEAD
from recruitment.models import Address, BTechExtras, Certification, Education, Internship, Job, Project, SocialProfile, StudentProfile
=======
from recruitment.models import Job,JobRound
>>>>>>> c50aa73 (written form to add-jobs)

class JobForm(forms.ModelForm):
    branches_allowed = SimpleArrayField(forms.CharField(max_length=10))
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['applied_by', 'num_of_students_applied']

<<<<<<< HEAD
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class BTechExtrasForm(forms.ModelForm):
    class Meta:
        model = BTechExtras
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class InternshipForm(forms.ModelForm):
    class Meta:
        model = Internship
        fields = '__all__'

class SocialProfileForm(forms.ModelForm):
    class Meta:
        model = SocialProfile
        fields = '__all__'
=======
class JobRoundForm(forms.ModelForm):
    class Meta:
        model = JobRound
        fields = '__all__'
>>>>>>> c50aa73 (written form to add-jobs)
