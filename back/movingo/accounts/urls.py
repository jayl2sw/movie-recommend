from . import views
from django.urls import path

app_name="accounts"

urlpatterns = [
    path('profile/<int:user_pk>/follow/', views.follow),
    path('profile/<username>/', views.profile),

]