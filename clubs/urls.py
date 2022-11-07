from django.urls import path

from .views import home, about, recruiting

urlpatterns = [
    path('home', home, name='home'),
    path('about/<int:id>', about, name='about'),
    path('event/<int:id>', about, name='event'),
    path('recruitment/<int:id>', recruiting, name='recruitment'),
]
