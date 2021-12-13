from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/profile', views.student_profile, name='student_profile'),
    path('student/edit', views.edit_profile, name='edit_profile'),
    path('student/edit/address', views.edit_address, name='edit_address'),
    path('student/edit/personal_information', views.edit_personal_info, name='edit_personal_information'),
    path('student/edit/education', views.edit_education, name='edit_education'),
    path('student/edit/experience', views.edit_experience, name='edit_experience'),
    path('student/edit/others', views.edit_others, name='edit_others'),
    path('student/applied', views.applied_jobs, name='applied_jobs'),
    path('student/apply/<str:company>/<int:job_id>', views.apply_to_job, name='apply_to_job'),

    path('recruiter/post', views.post_job, name='post_job'),
    path('manage/job/<int:job_id>/', views.manage_job, name='manage_job'),
    path('recruiter/hiringstatus', views.hiring_status, name='hiring_status'),

    path('stats', views.stats, name='stats'),

    # Django's internal views default to the accounts/login/. So, we define it to avoid any errors.
    path("register", views.register, name="register_page"),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]