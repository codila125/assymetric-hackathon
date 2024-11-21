from django.db import models
from django.utils import timezone

class arts(models.Model):
    date_added = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=100)
    built_date = models.DateTimeField()
    description = models.TextField()
    picture = models.ImageField(upload_to='website/arts_pics', blank=True)
    def __str__(self):
        return self.name
    
class places(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='website/places_pics', blank=True)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.name

