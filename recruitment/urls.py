from django.urls import path

from . import views

urlpatterns = [
    path('student/profile', views.student_profile, name='student_profile'),
    path('student/edit', views.edit_profile, name='edit_profile'),
    path('student/applied', views.applied_jobs, name='applied_jobs'),
    path('recruiter/register', views.recruiter_registration, name='recruiter_registration'),
    path('recruiter/post', views.post_job, name='post_job'),
    path('stats', views.stats, name='stats'),
]