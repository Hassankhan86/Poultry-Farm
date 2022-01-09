from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from expenses.models import Expenses
from medicine.models import medicine_data
from feed.models import FeedS16_Incoming, FeedS13_Incoming
from employee.models import SalaryPaid

@login_required(login_url='/accounts/login')
def expenses_view(request):
    total_expense = 0
    other_expenses = 0
    medical_expenses = 0
    feed_expenses = 0
    f_13_expenses = 0
    f_16_expenses = 0
    salary_expenses = 0
    salary_obj = SalaryPaid.objects.all()
    f_13_obj = FeedS13_Incoming.objects.all()
    f_16_obj = FeedS16_Incoming.objects.all()
    medicine_expenses_obj = medicine_data.objects.all()
    all_expenses = Expenses.objects.all()
    for salarys_paid in salary_obj.iterator():
        salary_expenses = salary_expenses + int(salarys_paid.amount)
    for s13_feed in f_13_obj.iterator():
        f_13_expenses = f_13_expenses + int(s13_feed.price)
    for s16_feed in f_16_obj.iterator():
        f_16_expenses = f_16_expenses + int(s16_feed.f16_price)
    for medicine in medicine_expenses_obj.iterator():
        medical_expenses = medical_expenses + int(medicine.price)
    for expense in all_expenses.iterator():
        other_expenses = other_expenses + int(expense.amount)
    feed_expenses = f_13_expenses + f_16_expenses
    total_expense = feed_expenses + medical_expenses + other_expenses + salary_expenses

    return render(request, 'expenses/expenses.html', {"all_expenses": all_expenses, "total_expense": total_expense,
                                                      "f_16_expenses": f_16_expenses,
                                                      "f_13_expenses": f_13_expenses,
                                                      "medical_expenses": medical_expenses,
                                                      "feed_expenses": feed_expenses,
                                                      "other_expenses": other_expenses,
                                                      "salary_expenses": salary_expenses})

@login_required(login_url='/accounts/login')
def add_expense(request):
    if request.method == 'POST':
        title = request.POST.get("expense")
        description = request.POST.get("expense_description")
        date = request.POST.get("date")
        amount = request.POST.get("amount")
        record = Expenses(title=title, date=date, description=description, amount=amount, updated_by=request.user)
        record.save()
        return expenses_view(request)
    return render(request, 'expenses/add_expenses.html', )

@login_required(login_url='/accounts/login')
def update_expenses(request, id):
    update_record = Expenses.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get("expense")
        description = request.POST.get("expense_description")
        date = request.POST.get("date")
        amount = request.POST.get("amount")

        update_record.title = title
        update_record.date = date
        update_record.amount = amount
        update_record.description = description
        update_record.save()
        return expenses_view(request)
    return render(request, 'expenses/update_expenses.html', {"update_record": update_record})

@login_required(login_url='/accounts/login')
def delete_expense(request, id):
    delete_expense = get_object_or_404(Expenses, id=id)
    delete_expense.delete()
    return expenses_view(request)

@login_required(login_url='/accounts/login')
def generated_expense(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        total_expense = 0
        other_expenses = 0
        medical_expenses = 0
        feed_expenses = 0
        f_13_expenses = 0
        f_16_expenses = 0
        salary_expenses = 0
        salary_obj = SalaryPaid.objects.filter(date__range=(from_date, to_date))
        f_13_obj = FeedS13_Incoming.objects.filter(date__range=(from_date, to_date))
        f_16_obj = FeedS16_Incoming.objects.filter(f16_date__range=(from_date, to_date))
        medicine_expenses_obj = medicine_data.objects.filter(date__range=(from_date, to_date))
        all_expenses = Expenses.objects.filter(date__range=(from_date, to_date))
        for salarys_paid in salary_obj.iterator():
            salary_expenses = salary_expenses + int(salarys_paid.amount)
        for s13_feed in f_13_obj.iterator():
            f_13_expenses = f_13_expenses + int(s13_feed.price)
        for s16_feed in f_16_obj.iterator():
            f_16_expenses = f_16_expenses + int(s16_feed.f16_price)
        for medicine in medicine_expenses_obj.iterator():
            medical_expenses = medical_expenses + int(medicine.price)
        for expense in all_expenses.iterator():
            other_expenses = other_expenses + int(expense.amount)
        feed_expenses = f_16_expenses + f_13_expenses
        total_expense = feed_expenses + medical_expenses + other_expenses + salary_expenses
        return render(request, 'expenses/expenses.html', {"all_expenses": all_expenses, "total_expense": total_expense,
                                                          "f_16_expenses": f_16_expenses,
                                                          "f_13_expenses": f_13_expenses,
                                                          "medical_expenses": medical_expenses,
                                                          "feed_expenses": feed_expenses,
                                                          "other_expenses": other_expenses,
                                                          "salary_expenses": salary_expenses})
    return render(request, 'expenses/generate_expenses_record.html', )
