from rest_framework import serializers
from . import models
from .models import Riot
from . import querry as q
from rest_framework.response import Response
from django.contrib.auth.models import User
from django import forms
from rest_framework.permissions import IsAdminUser


class RiotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riot
        fields = '__all__'
        read_only_fields=['response','user_profile']


class EarthquakeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=models.Earthquake
        fields='__all__'
        read_only_fields=['response','user_profile']


class CyberSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CyberCrime
        fields = '__all__'
        read_only_fields=['response','user_profile']


class TsunamiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Tsunami
        fields='__all__'
        read_only_fields=['response','user_profile']

class PollutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Severe_Pollution
        fields='__all__'
        read_only_fields=['response','user_profile']

class FloodSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Flood
        fields='__all__'
        read_only_fields=['response','user_profile']


class TerrorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Terrorism
        fields='__all__'
        read_only_fields=['response','user_profile']


class NuclearWarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.NuclearWar
        fields = '__all__'
        read_only_fields = ['response', 'user_profile']


class FireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Fire
        fields = '__all__'
        read_only_fields = ['response', 'user_profile']