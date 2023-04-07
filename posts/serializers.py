from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            # it means size > 2Mb
            raise serializers.ValidationError(
                'image size larger than 2Mb.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image hight larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return obj.owner == request.user

    class Meta:
        model = Post
        # fields = __all__
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'content',
            'image', 'is_owner', 'profile_id', 'profile_image', 'image_filter'
        ]
