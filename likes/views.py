from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadonly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

# Create your views here.
