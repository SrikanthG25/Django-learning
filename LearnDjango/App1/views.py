'''
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    UserData=[
        {"name":"Sri","age":21},
        {"name":"rish","age":25},
        {"name":"Sriram","age":22},
        {"name":"hari","age":12},
        {"name":"prem","age":18},
        
    ]
    return render(request,"index.html" ,{"Users":UserData})
    # return render(request,"index.html" , {'Name':'EMedHub'}) # to display view files into html

'''

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .serializers import StaffSerializer
from .models import Staffdata

@csrf_exempt
def staffAPI(request):
    if request.method == 'GET':
        Staff = Staffdata.objects.all()
        staff_serializer=StaffSerializer(Staff,many=True)
        return JsonResponse(staff_serializer.data,safe=False)

    elif request.method == 'POST':
        staff_detail = JSONParser().parse(request)
        staff_serializer=StaffSerializer(data=staff_detail)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse("Added Sucessfully",safe=False)
        return JsonResponse("Added Failed",safe=False)

@csrf_exempt
def StaffUpdate(request,id):
    if request.method == 'PUT':
        staff_detail = JSONParser().parse(request)
        Staff = Staffdata.objects.get(id=id)
        staff_serializer=StaffSerializer(Staff,data=staff_detail)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse("Update Sucessfully",safe=False)
        return JsonResponse("Update  Failed",safe=False)
    
    elif request.method == 'DELETE':
        Staff = Staffdata.objects.get(id=id)
        Staff.delete()
        return JsonResponse("Delete sucessfully",safe=False)



