from api.models import NewTags
from rest_framework_mongoengine import serializers


class NewTagsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = NewTags
        fields = '__all__'
