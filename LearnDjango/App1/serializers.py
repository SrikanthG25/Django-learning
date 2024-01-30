from rest_framework import serializers
from .models import Staffdata

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffdata
        fields = '__all__'