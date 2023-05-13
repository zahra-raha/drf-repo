from rest_framework import status, permissions, generics, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category
from .serializers import CategorySerializer
from drf_api.permissions import IsOwnerOrReadonly


class categoryListView(generics.ListCreateAPIView):
    """
    List categories or create a category if logged in
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Category.objects.annotate(
        posts_count=Count('post', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend
        ]
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'posts_count',
    ]


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a category and edit or delete it if you own it
    """
    permission_classes = [IsOwnerOrReadonly]
    serializer_class = CategorySerializer
    queryset = Category.objects.annotate(
        posts_count=Count('post', distinct=True)
    ).order_by('-created_at')
