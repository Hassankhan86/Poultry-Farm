from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from eggs.models import IncomingEggStock, OutgoingEggStock

@login_required(login_url='/accounts/login')
def eggs_record_details(request):
    all_incomings = IncomingEggStock.objects.all()
    all_outgoings = OutgoingEggStock.objects.all()
    incoming_quantity = 0
    outgoing_quantity = 0
    for eggs in all_incomings.iterator():
        incoming_quantity = eggs.quantity + incoming_quantity

    for eggs in all_outgoings.iterator():
        outgoing_quantity = eggs.quantity + outgoing_quantity

    instock_eggs = incoming_quantity - outgoing_quantity

    context = {"instock_eggs": instock_eggs, "all_outgoings": all_outgoings, "outgoing_quantity": outgoing_quantity,
               "all_incomings": all_incomings}
    return render(request, 'eggs/eggs_record_details.html', context)

@login_required(login_url='/accounts/login')
def add_incoming_eggs(request):
    if request.method == 'POST':
        quantity = request.POST.get("eggs_quantity")
        date = request.POST.get("date")
        record = IncomingEggStock(quantity=quantity, date=date, updated_by=request.user)
        record.save()
        return  eggs_record_details(request)
        # return redirect(eggs_record_details)
    return render(request, 'eggs/add_incoming_eggs.html', )

@login_required(login_url='/accounts/login')
def update_incoming_stock(request, id):
    update_record = IncomingEggStock.objects.get(id=id)
    if request.method == 'POST':
        quantity = request.POST.get("eggs_quantity")
        date = request.POST.get("date")
        update_record.quantity = quantity
        update_record.date = date
        update_record.save()
        return  eggs_record_details(request)
    return render(request, 'eggs/update_incoming_eggs.html', {"update_record": update_record})

@login_required(login_url='/accounts/login')
def delete_incoming_stock(request, id):
    obj = get_object_or_404(IncomingEggStock, id=id)
    obj.delete()
    return  eggs_record_details(request)

@login_required(login_url='/accounts/login')
def add_outgoing_eggs(request):
    if request.method == 'POST':
        quantity = request.POST.get("eggs_quantity")
        date = request.POST.get("date")
        amount = request.POST.get("amount")
        outgoing_record = OutgoingEggStock(quantity=quantity, date=date, rate=amount, updated_by=request.user)
        outgoing_record.save()
        return  eggs_record_details(request)
    return render(request, 'eggs/add_outgoing_eggs.html', )

@login_required(login_url='/accounts/login')
def update_outgoing_stock(request, id):
    update_record = OutgoingEggStock.objects.get(id=id)
    if request.method == 'POST':
        quantity = request.POST.get("eggs_quantity")
        date = request.POST.get("date")
        amount = request.POST.get("amount")
        update_record.quantity = quantity
        update_record.date = date
        update_record.rate = amount
        update_record.save()
        return  eggs_record_details(request)
    print(update_record.quantity)
    return render(request, 'eggs/update_outgoing_stock.html', {"update_record": update_record})

@login_required(login_url='/accounts/login')
def delete_outgoing_stock(request, id):
    obj = get_object_or_404(OutgoingEggStock, id=id)
    obj.delete()
    return  eggs_record_details(request)

@login_required(login_url='/accounts/login')
def generate_egg_slip(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")

        all_incomings = IncomingEggStock.objects.filter(date__range=(from_date, to_date))
        all_outgoings = OutgoingEggStock.objects.filter(date__range=(from_date, to_date))
        incoming_quantity = 0
        outgoing_quantity = 0
        for eggs in all_incomings.iterator():
            incoming_quantity = eggs.quantity + incoming_quantity

        for eggs in all_outgoings.iterator():
            outgoing_quantity = eggs.quantity + outgoing_quantity

        instock_eggs = incoming_quantity - outgoing_quantity

        context = {"instock_eggs": instock_eggs, "all_outgoings": all_outgoings, "outgoing_quantity": outgoing_quantity,
                   "all_incomings": all_incomings}
        return render(request, 'eggs/eggs_record_details.html', context)

    return render(request, 'eggs/generate_egg_slip.html', )
