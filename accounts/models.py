from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    
    username = models.CharField(max_length=40)
    image = models.ImageField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recruiter = models.BooleanField(blank=True, default=False)



@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
