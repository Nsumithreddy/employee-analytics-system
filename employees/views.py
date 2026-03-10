from django.shortcuts import render, redirect
from .models import Employee
import pandas as pd
import json

# Show employee dashboard
def employee_list(request):

    employees = Employee.objects.all()

    total_employees = employees.count()
    departments = employees.values('department').distinct().count()
    roles = employees.values('role').distinct().count()

    context = {
        'employees': employees,
        'total_employees': total_employees,
        'departments': departments,
        'roles': roles
    }

    return render(request, 'employees/employee_list.html', context)


# Add employee from website
def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['department']
        role = request.POST['role']
        date_joined = request.POST['date_joined']
        image = request.FILES.get('profile_image')

        Employee.objects.create(
        name=name,
        email=email,
        department=department,
        role=role,
        date_joined=date_joined,
        profile_image=image
        )
        return redirect('/')

    return render(request, 'employees/add_employee.html')
def edit_employee(request, id):

    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.department = request.POST['department']
        employee.role = request.POST['role']
        employee.date_joined = request.POST['date_joined']

        if request.FILES.get('profile_image'):
            employee.profile_image = request.FILES['profile_image']

        employee.save()

        return redirect('/')

    return render(request, 'employees/edit_employee.html', {'employee': employee})
def delete_employee(request, id):

    employee = Employee.objects.get(id=id)
    employee.delete()

    return redirect('/')

def analytics_dashboard(request):

    employees = Employee.objects.all().values()

    df = pd.DataFrame(list(employees))

    if df.empty:
        return render(request, 'employees/analytics.html', {'labels': [], 'data': []})

    dept_counts = df['department'].value_counts()

    labels = json.dumps(dept_counts.index.tolist())
    data = json.dumps(dept_counts.values.tolist())

    return render(request, 'employees/analytics.html', {
        'labels': labels,
        'data': data
    })