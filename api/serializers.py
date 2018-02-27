from api.models import Post, Tags
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'score', 'viewcount', 'tags', 'creationdate')


class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'count')
