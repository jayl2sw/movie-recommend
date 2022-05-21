# Create your views here.
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProfileSerializer


User = get_user_model()

@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(user)
    return Response(serializer.data)


def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk = user_pk)
    if user.followers.filter(pk=request.user.pk).exists():
        user.followers.remove(request.user)
        follow = False
    else:
        user.followers.add(request.user)
        follow = True

    serializer = ProfileSerializer(user)
    return Response(serializer.data)
    