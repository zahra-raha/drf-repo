from rest_framework import generics, filters
from django.db.models import Count
from .models import Profile
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadonly


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        followings_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile'
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'followings_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetails(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadonly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        followings_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
