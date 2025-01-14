
from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_employee, name='insert_employee'),
]
