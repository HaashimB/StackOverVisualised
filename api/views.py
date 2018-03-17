from rest_framework import viewsets
from api.models import Post, Tags
from api.serializers import PostSerializer, TagSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
        API Endpoint to view Post table
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagsViewSet(viewsets.ModelViewSet):
    """
        API Endpoint to view Tags table
    """
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
