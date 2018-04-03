from django.conf.urls import url, include
from api import views
from rest_framework_mongoengine import routers

router = routers.DefaultRouter()
router.register(r'tags', views.NewTagsViewSet, r'tags')
urlpatterns = [
    url(r'^', include(router.urls)),
]
