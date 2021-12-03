from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from .models import Profile


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
