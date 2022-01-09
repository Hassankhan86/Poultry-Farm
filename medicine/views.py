
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from medicine.models import *


# Create your views here.

@login_required(login_url='/accounts/login')
def medicine_list(request):
  data = medicine_data.objects.all()
  total_med_orders = medicine_data.objects.all().count()
  print(total_med_orders)
  total_med_price = 0
  for md in data:
    total_med_price = md.price + total_med_price
  print('Total_Feed_Income : ', total_med_price)
  context = {'data':data,'t_med_price':total_med_price,'TMO':total_med_orders,}

  return render(request, 'medicine_list.html',context)

  # return HttpResponse('<h1>Hello HttpResponse</h1>')


@login_required(login_url='/accounts/login')
def generate_medicine_slip(request):
  if request.method == "POST":
    from_date = request.POST.get("from_date")
    to_date = request.POST.get("to_date")

    data = medicine_data.objects.filter(date__range=(from_date, to_date))

    total_med_orders = medicine_data.objects.filter(date__range=(from_date, to_date)).count()
    print(total_med_orders)
    total_med_price = 0
    for md in data:
      total_med_price = md.price + total_med_price
    print('Total_Feed_Income : ', total_med_price)
    context = {'data': data, 't_med_price': total_med_price, 'TMO': total_med_orders, }

    return render(request, 'medicine_list.html', context)

  return render(request, 'generate_medicine_slip.html', )

@login_required(login_url='/accounts/login')
def medicine_add(request):
  Med_data = medicine_data()
  if request.method == 'POST':
    med_name = request.POST.get("med-name")
    med_quantity = request.POST.get("med-quantity")
    med_price = request.POST.get("med-price")
    med_date = request.POST.get("med-date")

    Med_data.name = med_name
    Med_data.quantity = med_quantity
    Med_data.price = med_price
    Med_data.date = med_date
    Med_data.updated_by = request.user
    Med_data.save()

    return medicine_list(request)

  return render(request, 'medicine_add.html')

@login_required(login_url='/accounts/login')
def medicine_update(request,pk):
  Med_data = medicine_data.objects.get(id=pk)
  if request.method == 'POST':
    med_name = request.POST.get("update-med-name")
    med_quantity = request.POST.get("update-med-quantity")
    med_price = request.POST.get("update-med-price")
    med_date = request.POST.get("update-med-date")

    Med_data.name = med_name
    Med_data.quantity = med_quantity
    Med_data.price = med_price
    Med_data.date = med_date
    Med_data.updated_by = request.user
    Med_data.save()


    return medicine_list(request)
  context = {'data': Med_data, }

  return render(request, 'medicine_update.html',context)

@login_required(login_url='/accounts/login')
def medicine_delete(request,id):
  obj = get_object_or_404(medicine_data, id=id)
  obj.delete()
  return medicine_list(request)
