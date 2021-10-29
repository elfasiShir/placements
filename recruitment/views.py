from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from recruitment.forms import JobForm
from recruitment.models import Job

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
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
    else:
        form = JobForm()
    return render(request, "recruitment/post-job.html", {'form': form})

def hiring_status(request):
    return render(request, "recruitment/hiring-status.html")

def manage_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        return render(request, "recruitment/manage-job.html", {'job': job})
    except Job.DoesNotExist:
        return render(request, "recruitment/manage-job.html", {'no_job_error': 'Job does not exist'})

def applied_jobs(request):
    return render(request, "recruitment/applied-jobs.html")

def stats(request):
    return render(request, "recruitment/stats.html")
