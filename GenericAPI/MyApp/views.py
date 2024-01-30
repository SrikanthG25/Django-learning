from django.shortcuts import render
from rest_framework import generics
from .models import MyModel
from .serializer import MyModelSerializer

# Create your views here.

class MyModelListCreateView(generics.ListCreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer

class MyModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer