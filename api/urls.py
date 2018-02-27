from django.conf.urls import url, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^stack/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^tags/', views.TagsView)
]
