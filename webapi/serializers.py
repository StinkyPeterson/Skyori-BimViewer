from rest_framework import serializers

from .models import User, Record, Indicator, ListIndicators, IFC



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'token')

class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        fields = '__all__' 