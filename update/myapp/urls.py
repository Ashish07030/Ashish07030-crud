
from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:employee_id>/', views.update_employee, name='update_employee'),
]
