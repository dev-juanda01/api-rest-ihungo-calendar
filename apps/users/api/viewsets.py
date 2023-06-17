from rest_framework import viewsets
from .serializers import UserSerializer, NotificationForUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()


class ActiveUsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.filter(is_active=True)
    allowed_methods = ['GET']


class NotificationForUserViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationForUserSerializer
    queryset = NotificationForUserSerializer.Meta.model.objects.all()
