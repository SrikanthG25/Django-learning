from django.shortcuts import render
from rest_framework import generics , status
from .serializers import ExcelSerializer
from .models import Excelmodel
from rest_framework.response import Response
import openpyxl
from django.http import HttpResponse

# class Register(generics.ListCreateAPIView):
#     queryset = Excelmodel.objects.all()
#     serializer_class = ExcelSerializer
class Register(generics.GenericAPIView):
    queryset = Excelmodel.objects.all()
    serializer_class = ExcelSerializer
    def get(self,request,pk=None):
        if pk is not None:
            data = Excelmodel.objects.filter(pk=id)
            serializers = ExcelSerializer(data=request.data)
            return Response(serializers.data , status=status.HTTP_302_FOUND)
        else:
            data = Excelmodel.objects.all()
            serializers = ExcelSerializer(data,data=request.data)
            return Response(serializers.data , status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ExcelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        
class ExportToExcelView(generics.GenericAPIView):
    def get(self, request,*args, **kwargs):
        data = Excelmodel.objects.all()
        data_dict = {
            'Name': [item.name for item in data],
            'Age': [item.age for item in data],
            'Description': [item.description for item in data],
        }
        data_df = pd.DataFrame(data_dict)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Book1.xlsx"'
        data_df.to_excel(response, index=False, engine='openpyxl')
        return response