from .models import Theater, Production, State
from rest_framework import serializers

class TheaterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theater
        fields = ['name','city','state']

class ProductionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Production
        fields = ['theater','show', 'start_date', 'end_date', 'description']

class StateNameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['abbr','name']