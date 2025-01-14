from django.shortcuts import render, redirect
from .models import EmployeeForm
from django.conf import settings



def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    employee = settings.EMPLOYEE_COLLECTION.find_one({"employee_id": employee_id})

    if request.method == 'POST':
        settings.EMPLOYEE_COLLECTION.delete_one({"employee_id": employee_id})
        return "success"

    return render(request, 'delete_form.html', {"employee": employee})



