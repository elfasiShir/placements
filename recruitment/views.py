from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist

from recruitment.forms import AddressForm, BTechExtrasForm, BacklogsAndEducationGapForm, CertificationForm, EducationForm, InternshipForm, JobForm, JobRoundForm, OthersForm, ProjectForm, SkillsForm, SocialProfileForm, StudentProfileForm
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

@login_required
def apply_to_job(request, company, job_id):
    # The `company` argument is just for readability in url.
    try:
        job = Job.objects.get(id=job_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Invalid request')

    # TODO: Add validation and check eligibility here

    job.applied_by.add(request.user)
    return render(request, 'recruitment/applied_success.html', context={'job': job})

@login_required
def applied_jobs(request):
    jobs_applied = request.user.applied_jobs.all()

    return render(request, "recruitment/applied-jobs.html", context={"jobs_applied": jobs_applied})

def edit_profile(request):
    if request.method == "POST":
        profileForm = StudentProfileForm(request.POST, request.FILES)
        permanentAddressForm = AddressForm(request.POST,prefix='permanent')
        hostelAddressForm = AddressForm(request.POST,prefix='hostel')
        pgForm = EducationForm(request.POST, request.FILES,prefix='pg')
        ugForm = EducationForm(request.POST, request.FILES,prefix='ug')
        interForm = EducationForm(request.POST, request.FILES,prefix='inter')
        tenthForm = EducationForm(request.POST, request.FILES,prefix='tenth')
        btechExtras = BTechExtrasForm(request.POST, request.FILES)
        certificatesCount = int(request.POST.get('certificate_count') or 0)
        internshipsCount = int(request.POST.get('internship_count') or 0)
        projectsCount = int(request.POST.get('project_count') or 0)
        socialProfilesCount = int(request.POST.get('social_profile_count') or 0)

        for i in range(certificatesCount):
            certForm = CertificationForm(request.POST, request.FILES,prefix='cert'+str(i))
            if certForm.is_valid():
                certForm.save()
            else:
                print('cf',i,  certForm.errors)

        for i in range(internshipsCount):
            internForm = InternshipForm(request.POST,prefix='internship'+str(i))
            if internForm.is_valid():
                internForm.save()
            else:
                print('if', i, interForm.errors)

        for i in range(projectsCount):
            proForm = ProjectForm(request.POST,prefix='project'+str(i))
            if proForm.is_valid():
                proForm.save()
            else:
                print('pr', i, proForm.errors)

        for i in range(socialProfilesCount):
            spForm = SocialProfileForm(request.POST,prefix='social'+str(i))
            if spForm.is_valid():
                spForm.save()
            else:
                print('sp', i, spForm.errors)

        for form in [profileForm, permanentAddressForm, hostelAddressForm, pgForm, ugForm, interForm, tenthForm, btechExtras]:
            if form.is_valid():
                form.save()
            else:
                print(form,form.errors)
    else:
        profileForm = StudentProfileForm()
        permanentAddressForm = AddressForm(prefix='permanent')
        hostelAddressForm = AddressForm(prefix='hostel')
        pgForm = EducationForm(prefix='pg')
        ugForm = EducationForm(prefix='ug')
        interForm = EducationForm(prefix='inter')
        tenthForm = EducationForm(prefix='tenth')
        btechExtras = BTechExtrasForm()
        certForm = CertificationForm(prefix='cert0')
        internForm = InternshipForm(prefix='internship0')
        proForm = ProjectForm(prefix='project0')
        spForm = SocialProfileForm(prefix='social0')

    return render(request, "recruitment/edit-student-profile.html")
def edit_address(request):
    if request.method == "POST":
        permanentAddressForm = AddressForm(request.POST,prefix='permanent')
        hostelAddressForm = AddressForm(request.POST,prefix='hostel')
        

        for form in [permanentAddressForm, hostelAddressForm]:
            if form.is_valid():
                form.save()
            else:
                print(form,form.errors)
    else:
        permanentAddressForm = AddressForm(prefix='permanent')
        hostelAddressForm = AddressForm(prefix='hostel')
    return render(request, "recruitment/student_profile/address.html")
def edit_personal_info(request):
    if request.method == "POST":
        profileForm = StudentProfileForm(request.POST, request.FILES)
        
        
        if profileForm.is_valid():
            profileForm.save()
        else:
            print(profileForm,profileForm.errors)
    else:
        profileForm = StudentProfileForm()
    return render(request, "recruitment/student_profile/personal_information.html")
def edit_education(request):
    if request.method == "POST":
        pgForm = EducationForm(request.POST, request.FILES,prefix='pg')
        ugForm = EducationForm(request.POST, request.FILES,prefix='ug')
        interForm = EducationForm(request.POST, request.FILES,prefix='inter')
        tenthForm = EducationForm(request.POST, request.FILES,prefix='tenth')
        btechExtras = BTechExtrasForm(request.POST, request.FILES)
        backlogsAndEduGap = BacklogsAndEducationGapForm(request.POST)
        

        for form in [pgForm, ugForm, interForm, tenthForm, btechExtras,backlogsAndEduGap]:
            if form.is_valid():
                form.save()
            else:
                print(form,form.errors)
    else:
        pgForm = EducationForm(prefix='pg')
        ugForm = EducationForm(prefix='ug')
        interForm = EducationForm(prefix='inter')
        tenthForm = EducationForm(prefix='tenth')
        btechExtras = BTechExtrasForm()
        backlogsAndEduGap = BacklogsAndEducationGapForm()
    return render(request, "recruitment/student_profile/education.html")
def edit_experience(request):
    if request.method == "POST":
        skillsForm = SkillsForm(request.POST, request.FILES)
        projectsCount = int(request.POST.get('project_count') or 0)
 
        for i in range(projectsCount):
            proForm = ProjectForm(request.POST,prefix='project'+str(i))
            if proForm.is_valid():
                proForm.save()
            else:
                print('pr', i, proForm.errors)

    

        for form in [skillsForm]:
            if form.is_valid():
                form.save()
            else:
                print(form,form.errors)
    else:
        skillsForm = SkillsForm()
        proForm = ProjectForm(prefix='project0')     
    return render(request, "recruitment/student_profile/experience.html")
def edit_others(request):
    if request.method == "POST":
        othersForm = OthersForm(request.POST)
        socialProfilesCount = int(request.POST.get('social_profile_count') or 0)

        for i in range(socialProfilesCount):
            spForm = SocialProfileForm(request.POST,prefix='social'+str(i))
            if spForm.is_valid():
                spForm.save()
            else:
                print('sp', i, spForm.errors)

        for form in [othersForm]:
            if form.is_valid():
                form.save()
            else:
                print(form,form.errors)
    else:
        othersForm = OthersForm()
        spForm = SocialProfileForm(prefix='social0')
    return render(request, "recruitment/student_profile/others.html")
def post_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.status = 'AO'  # Applications open
            job = form.save()
            return redirect(reverse('manage_job', kwargs={'job_id': job.id}))
    else:
        form = JobForm()
    return render(request, "recruitment/post-job.html", {'form': form})

def hiring_status(request):
    jobs = Job.objects.all()
    return render(request, "recruitment/hiring-status.html",{"jobs":jobs})

def manage_job(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        if request.method == "POST":
            form = JobRoundForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = JobRoundForm()
        job_rounds = job.job_rounds.filter()
        new_round_number = job_rounds.count() + 1
        return render(request, "recruitment/manage-job.html", {'job': job,
                                                               'form': form,
                                                                'job_rounds': job_rounds,
                                                                'new_round_number': new_round_number,
                                                                })
    except Job.DoesNotExist:
        return render(request, "recruitment/manage-job.html", {'no_job_error': 'Job does not exist'})

def stats(request):
    return render(request, "recruitment/stats.html")
