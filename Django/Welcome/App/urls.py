from django.urls import path
from .views import*
urlpatterns = [
    path('Register/',Register.as_view())
]