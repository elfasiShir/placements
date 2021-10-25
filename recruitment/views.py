from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))

    if request.user.from_tnp:
        return redirect(reverse('hiring_status'))

    return redirect(reverse('edit_profile'))

# TODO: Add @login_required to all views below this line.

def student_profile(request):
    return render(request, "recruitment/student-profile.html")

def edit_profile(request):
    return render(request, "recruitment/edit-student-profile.html")

def recruiter_registration(request):
    return render(request, "recruitment/recruiter-register.html")

def post_job(request):
    return render(request, "recruitment/post-job.html")

def hiring_status(request):
    return render(request, "recruitment/hiring-status.html")

def add_rounds(request):
    return render(request, "recruitment/add-rounds.html")

def applied_jobs(request):
    return render(request, "recruitment/applied-jobs.html")

def stats(request):
    return render(request, "recruitment/stats.html")
