from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.
@login_required(login_url='/accounts/login')
def birds_record_view(request):
    alive_birds = AliveBirdsRecords.objects.all()
    dead_birds = DeathBirdsRecords.objects.all()
    alive_birds_count = 0
    dead_birds_count = 0
    for birds in alive_birds.iterator():
        alive_birds_count = birds.birds_added + alive_birds_count
    for birds in dead_birds.iterator():
        dead_birds_count = birds.birds_died + dead_birds_count

    total_birds = alive_birds_count - dead_birds_count
    context = {"total_birds": total_birds, "dead_birds_count": dead_birds_count, "alive_birds": alive_birds,
               "dead_birds": dead_birds,
               "alive_birds_count": alive_birds_count}
    return render(request, 'birds/birds_record_view.html', context)
@login_required(login_url='/accounts/login')
def generate_birds_slip(request):
    if request.method == "POST":
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")
        alive_birds = AliveBirdsRecords.objects.filter(date__range=(from_date, to_date))
        dead_birds = DeathBirdsRecords.objects.filter(date__range=(from_date, to_date))
        alive_birds_count = 0
        dead_birds_count = 0
        for birds in alive_birds.iterator():
            alive_birds_count = birds.birds_added + alive_birds_count
        for birds in dead_birds.iterator():
            dead_birds_count = birds.birds_died + dead_birds_count

        total_birds = alive_birds_count - dead_birds_count
        context = {"total_birds": total_birds, "dead_birds_count": dead_birds_count, "alive_birds": alive_birds,
                   "dead_birds": dead_birds,
                   "alive_birds_count": alive_birds_count}
        return render(request, 'birds/birds_record_view.html', context)

    return render(request, 'birds/generate_birds_slip.html',)

@login_required(login_url='/accounts/login')
def add_more_alive_birds(request):
    if request.method == 'POST':
        no_of_birds = request.POST.get("no_of_birds")
        date = request.POST.get("date")
        record = AliveBirdsRecords(birds_added=no_of_birds, date=date, updated_by=request.user)
        record.save()
        return  birds_record_view(request)
        # return redirect(birds_record_view)
    return render(request, 'birds/add_more_alive_birds.html')

@login_required(login_url='/accounts/login')
def update_more_alive_birds(request, id):
    update_record = AliveBirdsRecords.objects.get(id=id)
    if request.method == 'POST':
        no_of_birds = request.POST.get("no_of_birds")
        date = request.POST.get("date")
        update_record.birds_added = no_of_birds
        update_record.date = date
        update_record.save()
        return  birds_record_view(request)
    return render(request, 'birds/update_more_alive_birds.html', {"update_record": update_record})

@login_required(login_url='/accounts/login')
def delete_alive_birds_record(request, id):
    obj = get_object_or_404(AliveBirdsRecords, id=id)
    obj.delete()
    return birds_record_view(request)

@login_required(login_url='/accounts/login')
def add_birds_deaths(request):
    if request.method == 'POST':
        no_of_birds = request.POST.get("no_of_birds")
        date = request.POST.get("date")
        record = DeathBirdsRecords(birds_died=no_of_birds, date=date, updated_by=request.user)
        record.save()
        return  birds_record_view(request)
    return render(request, 'birds/add_birds_deaths.html')

@login_required(login_url='/accounts/login')
def update_birds_deaths(request, id):
    update_record = DeathBirdsRecords.objects.get(id=id)
    if request.method == 'POST':
        no_of_birds = request.POST.get("no_of_birds")
        date = request.POST.get("date")
        update_record.birds_died = no_of_birds
        update_record.date = date
        update_record.save()
        return  birds_record_view(request)
    return render(request, 'birds/update_birds_death.html', {"update_record": update_record})

@login_required(login_url='/accounts/login')
def delete_dead_birds_record(request, id):
    obj = get_object_or_404(DeathBirdsRecords, id=id)
    obj.delete()
    return birds_record_view(request)
