from .models import Shift
from rest_framework import serializers

class ShiftSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = Shift
        # the fields that should be included in the serialized output
        fields = ['id', 'name', 'position', 'date', 'start_time', 'end_time']