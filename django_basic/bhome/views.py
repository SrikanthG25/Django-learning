'''

from django.shortcuts import render,redirect

from django.http import HttpResponse
from .models import data


def home(request):
    return HttpResponse("<h1>UNTOLD MYSTERY</h1>")

def name(request):
    return HttpResponse("<h1>UNTOLD MYSTERY</h1>")
    

def home(request):
    users=[
        {"Name":"sri","age":22},
        {"Name":"vicky","age":23},
        {"Name":"ganesh","age":24}
        ]
    employee=[
        {"Name":"sri","age":22},
        {"Name":"vicky","age":23},
        {"Name":"ganesh","age":24}
        ] 
    return render(request, "home.html",context={"users":users,"Emp":employee})


#home page
def product(request):
    return render(request,"product.html")

#result.html page
def result(request):
    lap=request.GET["laptop"]
    mod=request.GET["Model"]
    pri=request.GET["Price"]
    res=lap,mod,pri# to pass the value in nxt page
    return render(request,"result.html",{'Result':res})


def file(request):
    return render(request,"file.html")

def register(request):
    name=request.POST["name"]
    password=request.POST["password"]
    Address=request.POST["address"]
    Mail=request.POST["mail"]
    return render(request,"fileres.html",{'Name':name,'Pass':password,'add':Address,'mail':Mail})

def home1(request):
    return render(request,"home1.html")

def home2(request):
    return render(request,"home2.html")



def form(request):#127.0.0.1:8000/
    mydata=data.objects.all()
    if(mydata!=''):
        return render(request,"form.html",{'data':mydata})
    else:
        return render(request,"form.html")
def addData(request):#127.0.0.1:8000/addData
     if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        obj=data()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        mydata=data.objects.all()
        #return render(request,"form.html",{'data':mydata  })
        return redirect('form')
     return render(request,"form.html")

def updateData(request,id):#127.0.0.1:8000/updateData
    mydata=data.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        mail=request.POST['mail']

        mydata.Name=name
        mydata.Age=age
        mydata.Address=address
        mydata.Contact=contact
        mydata.Mail=mail
        mydata.save()

        return redirect('form')
    return render(request,'update.html',{'data':mydata})

def deleteData(request,id):
    mydata=data.objects.get(id=id)
    mydata.delete()
    return redirect('form')

    
'''

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .serializer import HomeSerializer
from .models import data
from django.http import HttpResponse

@csrf_exempt
def BasicAPI(request):
    if request.method == 'GET':
        home = data.objects.all()
        Home_serialiozer = HomeSerializer(home,many=True)
        return JsonResponse(Home_serialiozer.data,safe=False)
    elif request.method == 'POST':
        Home_details = JSONParser().parse(request)
        Home_serialiozer = HomeSerializer(data=Home_details)
        if Home_serialiozer.is_valid():
            Home_serialiozer.save()
            return JsonResponse("Added Sucessful",safe=False)
        return JsonResponse("Added Failed",safe=False)
    
@csrf_exempt
def BasicUpdate(request,id):
    if request.method == 'PUT':        
        Home_details = JSONParser().parse(request)
        home=data.objects.get(id=id)
        Home_serialiozer = HomeSerializer(home,data=Home_details)
        if Home_serialiozer.is_valid():
            Home_serialiozer.save()
            return JsonResponse("Updated Sucessful",safe=False)
        return JsonResponse("Update Failed",safe=False)
    
    elif request.method == 'DELETE':
        home=data.objects.get(id=id)
        home.delete()
        return JsonResponse("Delete Sucessfully",safe=False)

