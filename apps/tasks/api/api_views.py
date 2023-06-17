from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskListToUserSerializer
from apps.tasks.models import Task


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_task_api_view(request, user_id):
    user_tasks = TaskListToUserSerializer.Meta.model.objects.filter(
        user=user_id)

    if len(user_tasks) == 0:
        return Response({
            'message': 'Usuario sin tareas'
        }, status=status.HTTP_404_NOT_FOUND)
    else:
        users_serializer = TaskListToUserSerializer(user_tasks, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

        # return Response({
        #     'message': 'Usuario no existe'
        # }, status=status.HTTP_404_NOT_FOUND)
