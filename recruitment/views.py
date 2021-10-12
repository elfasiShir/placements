from django.shortcuts import render

# Create your views here.
def student_profile(request):
    return render(request, "recruitment/student-profile.html")

def edit_profile(request):
    return render(request, "recruitment/edit-student-profile.html")

def recruiter_registration(request):
    return render(request, "recruitment/recruiter-register.html")

def post_job(request):
    return render(request, "recruitment/post-job.html")

def applied_jobs(request):
    return render(request, "recruitment/applied-jobs.html")

def stats(request):
    return render(request, "recruitment/stats.html")
