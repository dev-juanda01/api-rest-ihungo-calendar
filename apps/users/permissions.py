from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .helpers.validators import authenticate_with_email
from .api.serializers import CustomObtainPairSerializer, UserSerializer


class Login(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('email', '')
        password = request.data.get('password', '')

        print(request.data)
        user = authenticate_with_email(email=username, password=password)
        print(user)

        if user and user.is_active:
            print('páso')
            login_serializer = self.serializer_class(data=request.data)

            if login_serializer.is_valid():
                print('paso 2')
                user_serializer = UserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'token-refresh': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión existoso'
                }, status=status.HTTP_200_OK)

            return Response({
                'error': 'Contraseña o correo invalidos'
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'error': 'Error al autenticarse - Consulte al admin'
        }, status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = UserSerializer.Meta.model.objects.filter(
            id=request.data('user', 0))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({
                'message': 'Sesión cerrada exisotosamente'
            })
        return Response({
            'message': 'No existe este usuario'
        })
