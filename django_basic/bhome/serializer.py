from rest_framework import serializers
from .models import data

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = '__all__'