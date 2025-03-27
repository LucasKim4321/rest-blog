from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # 필드 값을 리턴
    class Meta:
        model = User
        fields = ['id', 'username', 'email']