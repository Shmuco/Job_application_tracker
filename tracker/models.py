from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


# Create your models here.
class JobListing(models.Model):

    job_title = models.CharField(max_length=200)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=2000,)
    website = models.URLField(blank=True, null=True, unique=True)
    salary = models.TextField(max_length= 200, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True, null=True, default = timezone.now)

    class Meta:
        ordering = ['-created']
  

class Location(models.Model):
    name = models.CharField(max_length= 300)

    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']


    


class Company(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name.title()


class MyApplications(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    status_options = (
        ('INTERTESTED', 'intertested'), 
        ('APPLIED', 'applied'),  
        ('INTERVIEW', 'interview'),
        ('ACCEPTED', 'accepted'),
        ('REJECTED', 'rejected'),)
    status = models.CharField(max_length = 200, choices= status_options, default= 'INTERTESTED')

class Updates(models.Model):
    application = models.ForeignKey(MyApplications, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)