from api.models import FebJson, MarJson, JanJson, JanCsv
from rest_framework import viewsets
from api.serializers import FebJsonSerializer, MarJsonSerializer, JanJsonSerializer, JanCsvSerializer


class FebJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FebJsonSerializer
    queryset = FebJson.objects.all()


class MarJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MarJsonSerializer
    queryset = MarJson.objects.all()


class JanJsonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JanJsonSerializer
    queryset = JanJson.objects.all()


class JanCsvViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JanCsvSerializer
    queryset = JanCsv.objects.all()