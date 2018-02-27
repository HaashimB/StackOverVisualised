from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from api.models import Post
from api.serializers import PostSerializer
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))


class PostViewSet(viewsets.ModelViewSet):
    """
        API Endpoint to view Post table
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class TagsView:
#     with open(os.path.join(BASE, "./DATA/tags.json"), 'r') as f:
#         Tags = json.load(f)
#     print(Tags)


class TagsView(BrowsableAPIRenderer):
    def get_default_renderer(self, view):
        with open(os.path.join(BASE, "./DATA/tags.json"), 'r') as f:
            tags = json.load(f)
        return JSONRenderer()
