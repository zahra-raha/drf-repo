from rest_framework import status, permissions, generics
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadonly


class PostListView(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
