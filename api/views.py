from rest_framework import viewsets
from api.models import Post
from api.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
        API Endpoint to view Post table
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
