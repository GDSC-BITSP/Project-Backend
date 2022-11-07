from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

def upload_path_generator(instance, filename):
    return f'images/{instance.name}/{filename}'

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_path_generator, null=True)
    skill = TaggableManager()
    description = models.TextField()
    prev_work = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    por_txt = models.TextField()
    por_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True)
    recruit_link = models.URLField(max_length=200, null=True)
    event_details = models.TextField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField(blank= True, Null = True)
    name = models.CharField(max_length= 200)
    desc = models.TextField(max_length = 1024, blank=True)



