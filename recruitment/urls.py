from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('student/edit', views.edit_profile, name='edit_profile'),
    path('student/applied', views.applied_jobs, name='applied_jobs'),
    path('recruiter/register', views.recruiter_registration, name='recruiter_registration'),
    path('recruiter/post', views.post_job, name='post_job'),
    path('recruiter/rounds', views.add_rounds, name='add_rounds'),
    path('recruiter/hiringstatus', views.hiring_status, name='hiring_status'),
    path('stats', views.stats, name='stats'),

    # Django's internal views default to the accounts/login/. So, we define it to avoid any errors.
    path("register", views.register, name="register_page"),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]