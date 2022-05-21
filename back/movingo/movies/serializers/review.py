from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Review, Movie

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)
            
    user = UserSerializer(read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only = True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'like_users_cnt', 'rate', 'content', 'created_string',)
        read_only_fields = ('movie', )





