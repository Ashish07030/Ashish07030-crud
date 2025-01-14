
from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
