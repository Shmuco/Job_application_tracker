from django.db import models
from django.conf import settings

# Create your models here.
class Search(models.Model):
    query = models.CharField(max_length = 200)
    location = models.ForeignKey('tracker.Location', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null = True)
    time = models.DateTimeField(auto_now_add=True)

    
  