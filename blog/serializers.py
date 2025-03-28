from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Blog

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # 필드 값을 리턴
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=False)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'published_at', 'created_at', 'updated_at']