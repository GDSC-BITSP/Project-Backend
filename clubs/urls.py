from django.urls import path

from .views import home, about, recruiting, event

urlpatterns = [
    path('home', home, name='home'),
    path('about/<int:id>', about, name='about'),
    path('event/<int:id>', event, name='event'),
    path('recruitment/<int:id>', recruiting, name='recruitment'),
]
