from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tags', views.index(), r'tags')
urlpatterns = [
    url(r'^', include(router.urls)),
]
