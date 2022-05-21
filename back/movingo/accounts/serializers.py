from dataclasses import fields
from gc import collect
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie, Review
from collects.models import Collection
from bingos.models import Bingo

# 회원가입 코드
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    # profile_image 추가
    profile_image = serializers.ImageField(use_url=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['profile_image'] = self.validated_data.get('profile_image', '')

        return data


class ProfileSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('id', 'title', 'poster_path', 'original_title')

    class ReviewSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = ('pk', 'movie', 'rate', 'content', 'created_string',)

    class BingoSerializer(serializers.ModelSerializer):

        class Meta:
            model = Bingo 
            fields = ('pk',)

    class CollectionSerializer(serializers.ModelSerializer):
        
        class CollectionMovieSerializer(serializers.ModelSerializer):

            class Meta:
                model = Movie
                fields = ('pk', 'title', 'poster_path')

        movies = CollectionMovieSerializer(many=True)
        like_users_cnt = serializers.IntegerField(source='like_users.count', read_only = True)
        
        class Meta:
            model = Collection
            fields = ('pk', 'title', 'movies', 'like_users_cnt')

    class UserSerializer(serializers.ModelSerializer):
    
        class Meta:
            model= get_user_model()
            fields= ('pk', 'username')
    
    
    followers_cnt = serializers.IntegerField(source='followers.count', read_only = True)
    followings_cnt = serializers.IntegerField(source='followings.count', read_only = True)
    reviews_cnt = serializers.IntegerField(source='reviews.count', read_only = True)
    collections_cnt = serializers.IntegerField(source='collections.count', read_only = True)
    
    wish_movies = MovieSerializer(many=True)
    collections = CollectionSerializer(many=True)
    like_collections = CollectionSerializer(many=True)
    bingo_set = BingoSerializer(many=True)
    reviews = ReviewSerializer(many=True)


    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'nickname', 'wish_movies', 'like_collections', 'collections', 'reviews','bingo_set', 'followers_cnt', 'followings_cnt','reviews_cnt','collections_cnt', 'nickname', )

    
    
