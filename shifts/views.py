from .models import Shift
from rest_framework import viewsets, permissions, status
from .serializers import ShiftSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class ShiftViewSet(viewsets.ModelViewSet):
    # queryset is a list of all Shift objects
    queryset = Shift.objects.all()
    # serializer_class attribute is used to control which serializer class should be used for serializing & deserializing queryset & model instances
    serializer_class = ShiftSerializer
    # set permission_classes to allow unrestricted access to the api
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        # Generate and return a JWT token upon successful login
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_register(request):
    # Implement user registration logic here


@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)