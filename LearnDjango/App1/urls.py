from django.urls import path , include
from App1.views import *
from . import views


urlpatterns = [
    path('',views.staffAPI , name='staffAPI'),
    path('<int:id>/',views.StaffUpdate , name='StaffUpdate')

]