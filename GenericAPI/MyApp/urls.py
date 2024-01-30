from django.urls import path
from .views import MyModelListCreateView, MyModelDetailView

urlpatterns = [
    path('', MyModelListCreateView.as_view(), name='mymodel-list'),
    path('models/<int:pk>/', MyModelDetailView.as_view(), name='mymodel-detail'),
]