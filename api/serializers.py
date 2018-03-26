from api.models import Post, Tags
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'score', 'tags')


class TagSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tags
        fields = ('name', 'count')
