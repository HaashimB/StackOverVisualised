from api.models import NewTags
from rest_framework import viewsets
from api.serializers import TagsSerializer


class NewTagsViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''

    serializer_class = TagsSerializer
    queryset = NewTags.objects.all()
