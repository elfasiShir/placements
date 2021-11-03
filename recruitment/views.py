from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from recruitment.forms import JobForm
from recruitment.models import Job, User

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
