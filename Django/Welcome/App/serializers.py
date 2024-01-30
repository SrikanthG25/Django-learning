from rest_framework import serializers
from .models import Excelmodel

class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Excelmodel
        fields = '__all__'