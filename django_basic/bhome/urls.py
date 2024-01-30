from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',views.BasicAPI , name='BasicAPI'),
    path('<int:id>/',views.BasicUpdate , name='Basicupdate'),
]