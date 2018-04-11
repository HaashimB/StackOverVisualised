from api.models import FebJson, MarJson, JanJson
from rest_framework import viewsets
from api.serializers import FebJsonSerializer, MarJsonSerializer, JanJsonSerializer


class FebJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FebJsonSerializer
    queryset = FebJson.objects.all()


class MarJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MarJsonSerializer
    queryset = MarJson.objects.all()


class JanJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JanJsonSerializer
    queryset = JanJson.objects.all()

