from api.models import NewTags
from rest_framework_mongoengine import viewsets
from api.serializers import NewTagsSerializer


class NewTagsViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = NewTagsSerializer

    def get_queryset(self):
        return NewTags.objects.all()
