from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    posts_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        # fields = __all__
        fields = [
            'id', 'created_at', 'updated_at', 'name', 'icon', 'posts_count'
        ]

