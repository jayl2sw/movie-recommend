from dataclasses import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Collection, Hashtag
from movies.models import Movie, Genre



class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        field = ('tag')


class CollectionListSerializer(serializers.ModelSerializer):


    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model=get_user_model()
            fields = ('id', 'username',)
    
    class HashtagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Hashtag
            field = ('tag')

    like_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model= Collection
        fields= ('pk', 'user', 'title', 'like_users', 'hashtags','description', 'like_cnt')
        
    

class MainCollectionSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model=Movie
            fields = ('id', 'title', 'poster_path', 'vote_average', 'genres', 'original_title')

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model=get_user_model()
            fields = ('id', 'nickname')
    
    like_users = UserSerializer(many=True, read_only=True)
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model= Collection
        fields= ('pk', 'title', 'like_users', 'movies')
        
        

class CollectionDetailSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):

        class GenreSerializer(serializers.ModelSerializer):
            class Meta:
                model = Genre
                fields = ('id', 'name', )

        genres = GenreSerializer(many=True)

        class Meta:
            model=Movie
            fields = ('id', 'title', 'poster_path', 'backdrop_path', 'vote_average', 'genres')

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model=get_user_model()
            fields = ('id', 'username')
    
    class HashtagSerializer(serializers.ModelSerializer):
        class Meta:
            model = Hashtag
            field = ('tag')

    user = UserSerializer(read_only=True)
    like_users = UserSerializer(many=True, read_only=True)
    like_users_cnt = serializers.IntegerField(source='like_users.count', read_only=True)
    movies = MovieSerializer(many=True, read_only=True)
    hashtags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model= Collection
        fields= ('pk', 'title', 'movies', 'like_users_cnt', 'hashtags','description', 'user', 'like_users')
    
