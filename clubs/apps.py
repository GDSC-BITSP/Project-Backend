from django.apps import AppConfig


class ClubsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clubs'

class GoogleauthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GoogleAuth'
