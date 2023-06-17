from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def active_users_api_view(request):
    active_users = User.objects.filter(is_active=True)

    if len(active_users) == 0:
        return Response({
            'message': 'No hay usuarios activos'
        }, status=status.HTTP_404_NOT_FOUND)
    else:
        active_users_serializer = UserSerializer(active_users, many=True)
        return Response(active_users_serializer.data, status=status.HTTP_200_OK)
