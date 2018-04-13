from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'feb', views.FebJsonViewSet, r'feb')
router.register(r'mar', views.MarJsonViewSet, r'mar')
router.register(r'jan', views.JanJsonViewSet, r'jan')
router.register(r'jancsv', views.JanCsvViewSet, r'jancsv')

urlpatterns = [
    url(r'^', include(router.urls)),
]
