from django.contrib import admin

from clubs.models import Club, ClubHead, Event

admin.site.register(Club)
admin.site.register(Event)
admin.site.register(ClubHead)
