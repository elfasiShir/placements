from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'

    from_tnp = models.BooleanField(default=False)  # Everyone who's not from TnP is a student. Only they'll have a StudentProfile.
    mobile_number = models.CharField(max_length=10, blank=True)
    


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    roll_number = models.CharField(max_length=10, unique=True)
    registration_number = models.CharField(max_length=10, unique=True)
