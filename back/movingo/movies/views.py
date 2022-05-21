# articles/views.py
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review
from .serializers.movie import MovieListSerializer, MovieSerializer
from .serializers.review import ReviewSerializer

# from .serializers.review import CommentSerializer


@api_view(['GET'])
def movie_list(request):
    keyword = request.GET.get('keyword')

    if keyword:
        movies = Movie.objects.filter(title__contains=keyword).annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')
    else:
        movies = Movie.objects.annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')

    paginator = Paginator(movies, 20)
    page_number = request.GET.get('page')
    current_page = int(page_number) if page_number else 1

    movie_list = paginator.get_page(current_page)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_pk)

    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user, commit=False)
        serializer.rate = float(serializer.rate)
        # 기존 serializer 가 return 되면, 단일 comment 만 응답으로 받게됨.
        # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인 불가 => 업데이트된 전체 목록 return 
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def wish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.wish_users.filter(pk=user.pk).exists():
        movie.wish_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.wish_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

def movie_review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie=movie).annotate(likes_cnt=Count('like_users', distinct=True)).order_by('-likes_cnt')[:4]
    print(reviews.values())

    serializer = ReviewSerializer(reviews)
    return Response(serializer.data)

# @api_view(['PUT', 'DELETE'])
# def comment_update_or_delete(request, article_pk, comment_pk):
#     article = get_object_or_404(Article, pk=article_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     def update_comment():
#         if request.user == comment.user:
#             serializer = CommentSerializer(instance=comment, data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()
#                 comments = article.comments.all()
#                 serializer = CommentSerializer(comments, many=True)
#                 return Response(serializer.data)

#     def delete_comment():
#         if request.user == comment.user:
#             comment.delete()
#             comments = article.comments.all()
#             serializer = CommentSerializer(comments, many=True)
#             return Response(serializer.data)
    
#     if request.method == 'PUT':
#         return update_comment()
#     elif request.method == 'DELETE':
#         return delete_comment()
