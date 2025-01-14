from django.shortcuts import render, redirect
from .models import EmployeeForm
from django.conf import settings

def insert_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Insert the data into MongoDB
            settings.EMPLOYEE_COLLECTION.insert_one({
                'employee_id': form.cleaned_data['employee_id'],
                'name': form.cleaned_data['name'],
                'age': form.cleaned_data['age'],
                'position': form.cleaned_data['position'],
            })
            return "success"
    else:
        form = EmployeeForm()

    return render(request, 'insert_form.html', {'form': form})


