from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=500)
    department = models.CharField(max_length=150, blank=True)
    program = models.CharField(max_length=150, blank=True)
    year_of_study = models.IntegerField(null=True, blank=True)
    phone_no = models.TextField(max_length=11, blank=True)

    def __str__(self):
        return "Profile of %s" % self.user.username
