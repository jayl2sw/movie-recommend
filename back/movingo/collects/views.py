from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CollectionDetailSerializer, CollectionListSerializer, HashtagSerializer, MainCollectionSerializer
from datetime import datetime, timedelta, timezone
from .models import Collection, Hashtag
from movies.models import Movie

# Create your views here.
@api_view(['GET', 'POST'])
def collection_list_or_create(request):
    def collection_list():
        collections = Collection.objects.filter(on_main=False).annotate(like_cnt=Count('like_users', distinct=True)).order_by('-like_cnt')
        serializer = CollectionListSerializer(collections, many=True)
        return Response(serializer.data)

    def create_collection():
        # def create_hashtag():
        #     serializer = Hashtag(data=request.data)    
        #     if serializer.is_valid(raise_exception=True):
        #         serializer.save()
        #     return 

        # hashtags = get_list_or_404(Hashtag).tags()        
        # if 

        serializer = CollectionDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        return collection_list()
    elif request.method == 'POST':
        return create_collection()

@api_view(['GET','POST'])
def main_collections(request):
    collections = Collection.objects.annotate(
        like_cnt=Count('like_users')).filter(on_main=True).order_by('?')
    serializer = MainCollectionSerializer(collections, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def list_like_collection(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    collections = Collection.objects.filter(on_main=False).annotate(like_cnt=Count('like_users', distinct=True)).order_by('-like_cnt')
    user = request.user

    if collection.like_users.filter(pk=user.pk).exists():
        collection.like_users.remove(user)
        serializer = CollectionListSerializer(collections, many=True)
        return Response(serializer.data)
    else:
        collection.like_users.add(user)
        serializer = CollectionListSerializer(collections, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail_or_update_or_delete(request, collection_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)

    def article_detail():
        serializer = CollectionDetailSerializer(collection)
        return Response(serializer.data)

    def update_collection():
        if request.user == collection.user:
            serializer = CollectionDetailSerializer(instance=collection, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete_collection():
        if request.user == collection.user:
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        if request.user == collection.user:
            return update_collection()
    elif request.method == 'DELETE':
        if request.user == collection.user:
            return delete_collection()


@api_view(['POST'])
def add_movie(request, collection_pk, movie_pk):
    collection = get_object_or_404(Collection, pk=collection_pk)
    movie = get_object_or_404(Movie, pk = movie_pk)
    if collection.user == request.user:
        if not collection.movies.filter(id=movie_pk).exists():
            collection.movies.add(movie)
            serializer = CollectionDetailSerializer(collection)
            return Response(serializer.data)
    else:
        Response(status=status.HTTP_401_UNAUTHORIZED)
    

