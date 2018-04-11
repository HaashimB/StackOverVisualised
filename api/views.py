from api.models import NewTags
from rest_framework import viewsets
from api.serializers import TagsSerializer


class NewTagsViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = TagsSerializer
    queryset = NewTags.objects.all()
