# from api.models import NewTags
# from rest_framework import viewsets
# from api.serializers import NewTagsSerializer
#
#
# class NewTagsViewSet(viewsets.ModelViewSet):
#     '''
#     Contains information about inputs/outputs of a single program
#     that may be used in Universe workflows.
#     '''
#
#     serializer_class = NewTagsSerializer
#     queryset = NewTags.objects.all()


from django.http import HttpResponse


def index():
    return HttpResponse('./DATA/index.html')
