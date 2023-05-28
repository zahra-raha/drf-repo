from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadonly
from .models import Follow
from .serializers import FollowSerializer


class FollowList(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follow.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()


# Create your views here.
