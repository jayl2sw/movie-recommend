from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>', views.movie_detail),
    path('<int:movie_pk>/review', views.create_review),
    path('<int:movie_pk>/reviews', views.movie_review_list),
    path('<int:movie_pk>/wish', views.wish_movie),
]
