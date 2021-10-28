from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from recruitment.forms import AddressForm, BTechExtrasForm, CertificationForm, EducationForm, InternshipForm, JobForm, ProjectForm, SocialProfileForm, StudentProfileForm
from recruitment.models import BTechExtras, Job, User

def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.user.from_tnp:
        return redirect(reverse('hiring_status'))

    return redirect(reverse('edit_profile'))

def register(request):
    if request.method == 'POST':
        email = request.POST['user_email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        user = User.objects.create(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
    return render(request, 'registration/register.html')
    
# TODO: Add @login_required to all views below this line.

def student_profile(request):
    return render(request, "recruitment/student-profile.html")

def edit_profile(request):
    if request.method == "POST":
        profileForm = StudentProfileForm(request.POST, request.FILES,prefix='StudentProfile')
        permanentAddressForm = AddressForm(request.POST,prefix='permanentAddress')
        hostelAddressForm = AddressForm(request.POST,prefix='hostelAddress')
        pgForm = EducationForm(request.POST, request.FILES,prefix='postGraduation')
        ugForm = EducationForm(request.POST, request.FILES,prefix='underGraduation')
        interForm = EducationForm(request.POST, request.FILES,prefix='intermediate')
        tenthForm = EducationForm(request.POST, request.FILES,prefix='tenthGrade')
        btechExtras = BTechExtrasForm(request.POST, request.FILES,prefix='btechExtras')
        certificatesCount = request.POST['certificate-count']
        internshipsCount = request.POST['internship-count']
        projectsCount = request.POST['project-count']
        socialProfilesCount = request.POST['social-profile-count']
        for i in range(certificatesCount):
            certForm = CertificationForm(request.POST, request.FILES,prefix='certificate'+str(i))
            if certForm.is_valid():
                certForm.save()
        for i in range(internshipsCount):
            internForm = InternshipForm(request.POST,prefix='internship'+str(i))
            if internForm.is_valid():
                internForm.save()
        for i in range(projectsCount):
            proForm = ProjectForm(request.POST,prefix='project'+str(i))
            if proForm.is_valid():
                proForm.save()
        for i in range(socialProfilesCount):
            spForm = SocialProfileForm(request.POST,prefix='socialProfile'+str(i))
            if spForm.is_valid():
                spForm.save()

        if profileForm.is_valid() and permanentAddressForm.is_valid() and hostelAddressForm.is_valid() and pgForm.is_valid() and ugForm.is_valid() and interForm.is_valid() and tenthForm.is_valid() and btechExtras.is_valid():
            profileForm.save()
            permanentAddressForm.save()
            hostelAddressForm.save()
            pgForm.save()
            ugForm.save()
            interForm.save()
            tenthForm.save()
            btechExtras.save()
    else:
        form = StudentProfileForm()
    
    return render(request, "recruitment/edit-student-profile.html")

def recruiter_registration(request):
    return render(request, "recruitment/recruiter-register.html")

def post_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = JobForm()
    return render(request, "recruitment/post-job.html", {'form': form})

def hiring_status(request):
    jobs = Job.objects.all()
    return render(request, "recruitment/hiring-status.html",{"jobs":jobs})

def add_rounds(request):
    return render(request, "recruitment/add-rounds.html")

def applied_jobs(request):
    return render(request, "recruitment/applied-jobs.html")

def stats(request):
    return render(request, "recruitment/stats.html")
