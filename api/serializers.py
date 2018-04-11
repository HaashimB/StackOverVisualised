from api.models import FebJson, MarJson, JanJson
from rest_framework import serializers


class FebJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FebJson
        fields = ('id', 'content')


class MarJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarJson
        fields = ('id', 'content')


class JanJsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = JanJson
        fields = ('id', 'content')
