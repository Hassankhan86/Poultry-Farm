from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.


# @login_required(login_url='/accounts/login')
from employee.models import *


@login_required(login_url='/accounts/login')
def employee_list(request):
    Emp_data = employee_data.objects.all()
    total_emp = employee_data.objects.all().count()

    total_emp_salary = 0

    for EP in Emp_data:
        total_emp_salary = EP.emp_salary + total_emp_salary

    context = {'total_salary': total_emp_salary, 'TMO': Emp_data, 'total_emp': total_emp}

    return render(request, 'employee_list.html', context)


@login_required(login_url='/accounts/login')
def employee_add(request):
    Emp_data = employee_data()
    if request.method == 'POST':
        emp_name = request.POST.get("emp-name")
        emp_salary = request.POST.get("emp-salary")
        emp_cnic = request.POST.get("emp-cnic")
        emp_num = request.POST.get("emp-num")
        emp_Joining_date = request.POST.get("emp-Joining-date")

        Emp_data.emp_name = emp_name
        Emp_data.emp_salary = emp_salary
        Emp_data.emp_cnic = emp_cnic
        Emp_data.emp_num = emp_num
        Emp_data.emp_joining_date = emp_Joining_date

        Emp_data.updated_by = request.user
        Emp_data.save()

        return employee_list(request)

    return render(request, 'employee_add.html')


@login_required(login_url='/accounts/login')
def employee_update(request, pk):
    Emp_data = employee_data.objects.get(id=pk)

    if request.method == 'POST':
        emp_name = request.POST.get("emp-name")
        emp_salary = request.POST.get("emp-salary")
        emp_cnic = request.POST.get("emp-cnic")
        emp_num = request.POST.get("emp-num")
        emp_Joining_date = request.POST.get("emp-Joining-date")

        Emp_data.emp_name = emp_name
        Emp_data.emp_salary = emp_salary
        Emp_data.emp_cnic = emp_cnic
        Emp_data.emp_num = emp_num
        Emp_data.emp_joining_date = emp_Joining_date

        Emp_data.updated_by = request.user
        Emp_data.save()

        return employee_list(request)
    context = {'Emp_data': Emp_data}

    return render(request, 'employee_update.html', context)


@login_required(login_url='/accounts/login')
def employee_delete(request, id):
    obj = get_object_or_404(employee_data, id=id)
    obj.delete()
    return employee_list(request)

def paid_salary_record(request):
    salary_record = SalaryPaid.objects.all()
    total_paid_salary = 0
    for salary in salary_record.iterator():
        total_paid_salary = total_paid_salary + int(salary.amount)
    context = {"salary_record": salary_record, "total_paid_salary": total_paid_salary}
    return render(request, 'paid_salary_record.html', context)


@login_required(login_url='/accounts/login')
def pay_salary(request):
    if request.method == "POST":
        salary_paid = request.POST.get('salary_paid')
        date = request.POST.get('date')
        salary_obj = SalaryPaid(amount=salary_paid, date=date, updated_by=request.user)
        salary_obj.save()
        return paid_salary_record(request)
    return render(request, 'pay_salary.html', )

@login_required(login_url='/accounts/login')
def update_salary_paid_record(request, id):
    salary_record = SalaryPaid.objects.get(id=id)
    if request.method == 'POST':
        salary_paid = request.POST.get('salary_paid')
        date = request.POST.get('date')
        salary_record.amount = salary_paid
        salary_record.date = date
        salary_record.save()
        return paid_salary_record(request)
    context = {'salary_record': salary_record}
    return render(request, 'salary_record_update.html', context)

@login_required(login_url='/accounts/login')
def delete_salary_paid_record(request, id):
    salary_record = get_object_or_404(SalaryPaid, id=id)
    salary_record.delete()
    return paid_salary_record(request)
