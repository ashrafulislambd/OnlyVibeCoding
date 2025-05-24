from django.db import models

class Profile(models.Model):
    university = models.CharField(max_length=500)
    department = models.CharField(max_length=150)
    program = models.CharField(max_length=150)
    year_of_study = models.IntegerField()
    phone_no = models.TextField(max_length=11)
