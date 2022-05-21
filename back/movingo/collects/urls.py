from django.urls import path
from . import views

app_name="collections"

urlpatterns = [
    path('', views.collection_list_or_create),
    path('main/', views.main_collections),
    path('<int:collection_pk>/', views.collection_detail_or_update_or_delete),
    # path('<int:collection_pk>/like/', views.list_like_collection),
    path('<int:collection_pk>/like/list/', views.list_like_collection),
    path('<int:collection_pk>/add/<int:movie_pk>/', views.add_movie),
]
