from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Club, ClubHead, Event


@api_view(['GET'])
def home(request):
    clubs = []
    depts = []
    assocs = []
    techteams = []
    for club in Club.objects.all():
        imgurl = ""
        try:
            imgurl = club.logo.url
        except ValueError:
            imgurl = ""
        if club.type == 'club':
            clubs.append({
                'id': club.id,
                'name': club.name,
                'img': imgurl
            })
        elif club.type == 'department':
            depts.append({
                'id': club.id,
                'name': club.name,
                'img': imgurl
            })
        elif club.type == 'assoc':
            assocs.append({
                'id': club.id,
                'name': club.name,
                'img': imgurl
            })
        elif club.type == 'techteam':
            techteams.append({
                'id': club.id,
                'name': club.name,
                'img': imgurl
            })
    return Response({
        'clubs': clubs,
        'departments': depts,
        'assocs': assocs,
        'techteam': techteams
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
        imgurl = ""
        try:
            imgurl = event.img.url
        except ValueError:
            imgurl = ""
        events.append({
            'id': event.id,
            'name': event.name,
            'description': event.desc,
            'date': event.date,
            'image': imgurl
        })
    clubheads = []
    for clubhead in ClubHead.objects.all():
        imgurl = ""
        try:
            imgurl = clubhead.img.url
        except ValueError:
            imgurl = ""
        clubheads.append({
            'name': clubhead.name,
            'por': clubhead.POR,
            'image': imgurl
        })

    return Response({
        'name': club.name,
        'logo': club.logo.url,
        'skills': [tag.name for tag in club.skill.all()],
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
        'club_name': event.club.name,
        'event_name': event.name,
        'date': event.date
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def recruiting(request, id):
    try:
        club = Club.objects.get(id=id)
    except ObjectDoesNotExist:
        return Response({
            'message': 'Error! No such club exists in the database'
        }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'name': club.name,
        'recruit_link': club.recruit_link,
        'recruit_desc': club.recruit_desc,
        'recruiting': club.is_recruiting
    })
