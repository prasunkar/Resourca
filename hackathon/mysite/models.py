from django.db import models
from django.contrib.auth.models import User
class submissions(models.Model):
    summary=models.CharField(max_length=2000)

class Resource(models.Model):
    name = models.CharField(max_length=50)
    questions = models.FileField()
    answers = models.FileField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=50)
    prov_choices = [
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('ON', 'Ontario'),
        ('AL', 'Alberta'),
        ('MB', 'Manitoba'),
        ('SK', 'Saskatchewan'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NS', 'Nova Scotia'),
        ('NB', 'New Brunswick'),
    ]
    province = models.CharField(max_length=50, choices=prov_choices)

# class Pin(models.Model):
#     prof = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     file = models.ForeignKey(???, on_delete=models.CASCADE)
