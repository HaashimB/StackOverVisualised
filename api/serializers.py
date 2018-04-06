from api.models import NewTags
from rest_framework import serializers


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTags
        fields = 'content'
