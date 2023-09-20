from .models import Shift
from rest_framework import viewsets, permissions
from .serializers import ShiftSerializer

# Create your views here.

class ShiftViewSet(viewsets.ModelViewSet):
    # queryset is a list of all Shift objects
    queryset = Shift.objects.all()
    # serializer_class attribute is used to control which serializer class should be used for serializing & deserializing queryset & model instances
    serializer_class = ShiftSerializer
    # set permission_classes to allow unrestricted access to the api
    permission_classes = [permissions.AllowAny]