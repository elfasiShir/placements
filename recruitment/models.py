from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from recruitment.lib.file_path import certificate_path, certifications_path, marksheet_path, resume_path

BRANCHES = (
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('CIVIL', 'Civil Engineering'),
        ('CHEM', 'Chemical Engineering'),
        ('BIOT', 'Biotechnology'),
        ('MME', 'Metallurgical and Materials Engineering'),
    )

class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'

    from_tnp = models.BooleanField(default=False)  # Everyone who's not from TnP is a student. Only they'll have a StudentProfile.
    mobile_number = models.CharField(max_length=10, blank=True)
    

class Address(models.Model):
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    country = models.CharField(max_length=100)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll_number = models.CharField(max_length=10, unique=True)
    registration_number = models.CharField(max_length=10, unique=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    PROGRAMME_CHOICES = (
        ('B.Tech', 'Bachelor of Technology'),
        ('M.Tech', 'Master of Technology'),
    )
    programme = models.CharField(max_length=10, choices=PROGRAMME_CHOICES)

    FIELD_OF_STUDY_CHOICES = BRANCHES
    field_of_study = models.CharField(max_length=10)

    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)

    BACKLOGS_STATUS = (
        ('NB', 'No backlogs'),
        ('NOB', 'No outstanding backlogs'),
        ('OB', 'Outstanding backlogs'),
    )
    backlogs_status = models.CharField(max_length=3, default='NB')

    gap_in_education = models.BooleanField()
    reason_for_gap_in_education = models.TextField()

    resume = models.FileField(resume_path)
    achievements = models.TextField('Awards/Recognitions received')
    publications = models.TextField('Papers published')
    hackathons_participated = models.TextField('Hackathons Participated')
    extra_curricular_activities = models.TextField('Extra Curricular Activities')


class Education(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    institute = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)  # eg. B.Tech, M.Tech; Use as board for inter/10th.
    field_of_study = models.CharField(max_length=100, null=True)  # cse, ece, etc. for ug/pg; MPC, BiPC etc for inter; NULL for 10th
    year_of_passing = models.CharField(max_length=4)
    year_of_enrollment = models.CharField(max_length=4)

    LEVEL_CHOICES = (
        ('10th', '10th'),
        ('inter', 'Intermediate or 11th, 12th'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
    )
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)

    SCORE_TYPE_CHOICES = (
        ('CGPA', 'CGPA'),
        ('PERCENTAGE', 'Percentage'),
    )
    score_type = models.CharField(max_length=10, choices=SCORE_TYPE_CHOICES)  # percentage or CGPA
    score = models.FloatField()

    PASSING_CLASS_CHOICES = (
        ('Distinction', 'Distinction'),
        ('First', 'First Class'),
        ('Second', 'Second Class'),
        ('Third', 'Third Class'),
    )
    passing_class = models.CharField(max_length=11, choices=PASSING_CLASS_CHOICES, null=True, blank=True)

    certificate = models.FileField(upload_to=certificate_path, null=True, blank=True)
    marksheet = models.FileField(upload_to=marksheet_path, null=True, blank=True)

class Certification(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certifications')
    name = models.CharField('Certification name', max_length=128)
    issuing_authority = models.CharField(max_length=128)
    certificate = models.FileField(upload_to=certifications_path, blank=True, null=True)

class Project(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField('Project title', max_length=128)
    is_team_project = models.BooleanField()
    description = models.TextField()

class Internship(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='internships')
    role = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    duration = models.CharField(max_length=128)
    description = models.TextField()

class SocialProfile(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_profiles')
    name = models.CharField('Name of the site. Like GitHub, LinkedIn etc.', max_length=128)
    link = models.URLField()

class Job(models.Model):
    title = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    description = models.TextField('Job description')
    description_link = models.URLField()
    ctc = models.DecimalField('Cost to Company', max_digits=5, decimal_places=2)
    location = models.CharField('Job location', max_length=128)

    QUALIFICATION_CHOICES = (
        ('B.Tech', 'Bachelor of Technology'),
        ('M.Tech', 'Master of Technology'),
    )
    minimum_qualification = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
    year_of_graduation = models.CharField(max_length=4)

    mandatory_skills = models.TextField()
    desirable_skills = models.TextField()

    ug_cutoff = models.DecimalField('Undergraduate CGPA cutoff', max_digits=4, decimal_places=2)
    masters_cutoff = models.DecimalField('Masters CGPA cutoff', max_digits=4, decimal_places=2)

    backlogs_allowed = models.BooleanField()
    max_num_of_backlogs_allowed = models.SmallIntegerField('Maximum number of backlogs allowed', null=True, default=None)  # None for any nymber of backlogs allowed
    
    branches_allowed = ArrayField(models.CharField(max_length=10, choices=BRANCHES))

    files = ArrayField(models.FileField('Attached file'))
    deadline = models.DateTimeField()

    hr_name = models.CharField(max_length=128)
    hr_email = models.EmailField()
    hr_phone = models.CharField(max_length=15)

class JobRound(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_rounds')
    round_number = models.SmallIntegerField('Round number')
    start_time = models.DateTimeField()
    deadline = models.DateTimeField()
    selected = models.ManyToManyField(User)
    description = models.TextField()

    contact_num = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

class JobAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_alerts')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_alerts')
    created_at = models.DateTimeField(auto_now_add=True)