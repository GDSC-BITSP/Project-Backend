from .models import Club
from rest_framework import serializers

class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'