from api.models import Posts, Tags
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ('id', 'score', 'viewcount', 'tags', 'creationdate')


class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'count')
