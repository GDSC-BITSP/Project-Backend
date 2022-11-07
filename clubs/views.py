from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Club


@api_view(['GET'])
def home(request):
    clubs = []
    for club in Club.objects.all():
        clubs.append({
            'id': club.id,
            'name': club.name,
            'img': club.logo
        })
    return Response({
        clubs
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def about(request):
    club =
