from django import forms

class EmployeeForm(forms.Form):
    employee_id = forms.IntegerField(label='Employee ID')
    name = forms.CharField(label='Name',max_length=100)
    age = forms.CharField(label='Age')
    position = forms.CharField(label='Position',max_length=100)
