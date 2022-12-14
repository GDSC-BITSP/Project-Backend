from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


def upload_path_generator(instance, filename):
    return f'clubs/{instance.name}/{filename}'


def upload_path_generator2(instance, filename):
    return f'events/{instance.name}/{filename}'


def upload_path_generator3(instance, filename):
    return f'clubheads/{instance.name}/{filename}'


class Club(models.Model):
    TYPE_CHOICES = (
        ('club', 'club'),
        ('department', 'department'),
        ('assoc', 'assoc'),
        ('techteam', 'techteam')
    )
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default='club')
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=upload_path_generator, null=True)
    skill = TaggableManager()
    description = models.TextField()
    prev_work = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    por_txt = models.TextField(blank=True, null=True)
    por_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null=True, blank=True)
    recruit_link = models.URLField(max_length=200, null=True, blank=True)
    recruit_desc = models.TextField(max_length=200, null=True, blank=True)
    last_updated = models.DateTimeField(default=timezone.now)
    is_recruiting = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=1024, blank=True)
    img = models.ImageField(upload_to=upload_path_generator2, blank=True, null=True)


class ClubHead(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    POR = models.CharField(max_length=1024, blank=True)
    img = models.ImageField(upload_to=upload_path_generator3, blank=True, null=True)
