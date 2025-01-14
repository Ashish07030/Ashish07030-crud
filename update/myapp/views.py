from django.shortcuts import render, redirect
from .models import EmployeeForm
from django.conf import settings


def update_employee(request, employee_id):
    employee_id = int(employee_id)
    employee = settings.EMPLOYEE_COLLECTION.find_one({"employee_id": employee_id})

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            updated_data = {
                "employee_id": int(request.POST['employee_id']),
                "name": request.POST['name'],
                "age": int(request.POST['age']),
                "position": request.POST['position'],
            }
            settings.EMPLOYEE_COLLECTION.update_one({"employee_id": employee_id}, {"$set": updated_data})
            print("updated")
            return "success"
    else:
        pre_filled_data = {
            "employee_id": employee.get("employee_id"),
            "name": employee.get("name"),
            "age": employee.get("age"),
            "position": employee.get("position"),
        }
        form = EmployeeForm(initial=pre_filled_data)

    return render(request, 'update_form.html', {"form": form})



