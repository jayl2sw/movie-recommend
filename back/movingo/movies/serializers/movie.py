from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('pk', 'name',)

class MovieListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    wish_users = UserSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model=Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'vote_average','original_title', 'wish_users', 'genres')
        


class MovieSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    class RelatesSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('pk', 'title', 'poster_path')

    wish_users = UserSerializer(many=True)
    wish_count = serializers.IntegerField(source='wish_users.count', read_only=True)
    reviews_cnt = serializers.IntegerField(source='reviews.count', read_only=True)
    genres = GenreSerializer(many=True)
    related_movies = RelatesSerializer(many=True)
    
    class Meta:
        model=Movie
        fields = ('pk', 'title', 'overview', 'release_date', 'original_title','poster_path', 'backdrop_path', 'vote_average', 'reviews_cnt',
        'vote_count', 'popularity', 'adult', 'view_cnt', 'genres', 'related_movies', 'wish_users','wish_count',)    
    