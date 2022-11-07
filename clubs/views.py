import status as status
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Club, ClubHead, Event


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
def about(request, id):
    try:
        club = Club.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response({
            'message': 'Error! Club with given id does not exist in the database'
        }, status=status.HTTP_404_NOT_FOUND)

    events = []
    for event in club.event_set.all():
        events.append({
            'name': event.name,
            'description': event.desc,
            'date': event.date,
            'image': event.img
        })
    clubheads = []
    for clubhead in ClubHead.objects.all():
        clubheads.append({
            'name': clubhead.name,
            'por': clubhead.POR,
            'image': clubhead.img
        })

    return Response({
        'name': club.name,
        'logo': club.logo,
        'skills': [tag for tag in club.skill.all()],
        'description': club.description,
        'events': events,
        'recruitment_description': club.recruit_desc,
        'recruitment_link': club.recruit_link,
        'clubheads': clubheads,

    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def event(request, id):
    try:
        event = Event.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response({
            'message': 'Error! Event with given id does not exist in the database'
        }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'club_name': event.club,
        'event_name': event.name,
        'date': event.date
    }, status=status.HTTP_200_OK)

