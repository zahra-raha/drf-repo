from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadonly
from .models import Post


class PostListView(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
            )
        return Response(serializer.data)

    def post(self, request):
        serializer_class = PostSerializer
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadonly]

    def get_obj(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            return post

        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_obj(pk)
        serializer = PostSerializer(post, context={'request':request})
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_obj(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request':request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_obj(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

# Create your views here.
