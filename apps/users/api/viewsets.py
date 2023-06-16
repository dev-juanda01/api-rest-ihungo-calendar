from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, NotificationForUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    # permission_classes = (IsAuthenticated,)


"""
class ActivePartnersViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = PartnerSerializer.Meta.model.objects.filter(is_active=True)
    allowed_methods = ['GET']
"""


class NotificationForUserViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationForUserSerializer
    queryset = NotificationForUserSerializer.Meta.model.objects.all()
