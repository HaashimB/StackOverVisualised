from rest_framework import viewsets
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from api.models import Posts, Tags
from api.serializers import PostSerializer, TagSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
        API Endpoint to view Post table
    """
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# class TagsView:
#     with open(os.path.join(BASE, "./DATA/tags.json"), 'r') as f:
#         Tags = json.load(f)
#     print(Tags)


class TagsViewSet(BrowsableAPIRenderer):
    """
        API Endpoint to view Tags table
    """
