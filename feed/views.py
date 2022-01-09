from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from feed.models import *


# Create your views here.

@login_required(login_url='/accounts/login')
def dashboard(request):
  return render(request, 'Homepage.html')

  # return HttpResponse('<h1>Hello HttpResponse</h1>')


@login_required(login_url='/accounts/login')
def feed_add(request):
  Feed13 = FeedS13_Incoming()
  if request.method == 'POST':
    Date = request.POST.get("feed-date")
    Quantity = request.POST.get("feed-quantity")
    Price = request.POST.get("feed-price")
    # sex = request.POST.get("gender")

    Feed13.date = Date
    Feed13.quantity = Quantity
    Feed13.price = Price
    Feed13.updated_by = request.user
    Feed13.save()
    print(Quantity)
    print(Date)
    return feed_details(request)

  return render(request, 'feed_add.html')

@login_required(login_url='/accounts/login')
def generate_feed_slip(request):
  if request.method == "POST":
    from_date = request.POST.get("from_date")
    to_date = request.POST.get("to_date")
    print(from_date)
    print(to_date)
    Feeds13_Incoming = FeedS13_Incoming.objects.filter(date__range=(from_date, to_date))
    Feeds13_outgoing = FeedS13_Outgoing.objects.filter(date__range=(from_date, to_date))

    FS16_in = FeedS16_Incoming.objects.filter(f16_date__range=(from_date, to_date))
    FS16_out = FeedS16_Outgoing.objects.filter(f16_date__range=(from_date, to_date))

    Total_FeedS13_Income = 0
    Total_FeedS16_Income = 0
    for feeds1 in Feeds13_Incoming:
      Total_FeedS13_Income = feeds1.quantity + Total_FeedS13_Income

    for feedso in FS16_in:
      Total_FeedS16_Income = feedso.f16_quantity + Total_FeedS16_Income
    context = {'fs13_in': Feeds13_Incoming, 'Total_Feed_Income': Total_FeedS13_Income, "fs13_out": Feeds13_outgoing,
               'FS16_in': FS16_in, 'FS16_out': FS16_out, 'Total_FeedS16_Income': Total_FeedS16_Income}
    # context = {'f_16_price':f_16_price,'f_13_price':f_13_price,'total_feed_expense':total_feed_expense,'F13_obj':F13_obj,'F16_obj':F16_obj}
    return render(request, 'feed_details.html', context, )

  return render(request, 'generate_feed_slip.html', )


@login_required(login_url='/accounts/login')
def feed_details(request):
  Feeds13_Incoming = FeedS13_Incoming.objects.all()
  Feeds13_outgoing = FeedS13_Outgoing.objects.all()

  FS16_in = FeedS16_Incoming.objects.all()
  FS16_out = FeedS16_Outgoing.objects.all()

  Total_FeedS13_Income = 0
  for feeds1 in Feeds13_Incoming:
    Total_FeedS13_Income = feeds1.quantity + Total_FeedS13_Income
  print('Total_Feed_Income : ', Total_FeedS13_Income)

  Total_FeedS16_Income = 0
  for feedso in FS16_in:
    Total_FeedS16_Income = feedso.f16_quantity + Total_FeedS16_Income
  print('Total_FeedS16_Income : ', Total_FeedS16_Income)

  # Remain_feed = Total_Feed_Income - Total_Feed_out
  # print('Remain_feed : ',Remain_feed)

  context = {'fs13_in': Feeds13_Incoming, 'Total_Feed_Income': Total_FeedS13_Income, "fs13_out": Feeds13_outgoing,
             'FS16_in': FS16_in, 'FS16_out': FS16_out, 'Total_FeedS16_Income': Total_FeedS16_Income}

  return render(request, 'feed_details.html', context)


@login_required(login_url='/accounts/login')
def feed_update(request, pk):
  update_feed = FeedS13_Incoming.objects.get(id=pk)
  print('employee :', update_feed.price)
  print(update_feed.price)
  print(update_feed.date)
  print(update_feed.quantity)
  if request.method == 'POST':
    Date = request.POST.get("up_feed-date")
    Quantity = request.POST.get("up_feed-quantity")
    Price = request.POST.get("up_feed-price")
    # sex = request.POST.get("gender")

    update_feed.date = Date
    update_feed.quantity = Quantity
    update_feed.price = Price
    # update_feed.updated_by = request.user
    update_feed.save()
    return feed_details(request)

  context = {'update_feed': update_feed}

  return render(request, 'feed_update.html', context)


@login_required(login_url='/accounts/login')
def Feed_delete(request, id):
  obj = get_object_or_404(FeedS13_Incoming, id=id)
  obj.delete()
  return feed_details(request)


@login_required(login_url='/accounts/login')
def feed_s13_out_add(request):
  Feed13_Out = FeedS13_Outgoing()
  if request.method == 'POST':
    Date = request.POST.get("feed-out-date")
    Quantity = request.POST.get("feed-out-quantity")
    # sex = request.POST.get("gender")

    # print(Date)
    # print(Quantity)
    Feed13_Out.date = Date
    Feed13_Out.quantity = Quantity
    Feed13_Out.updated_by = request.user
    Feed13_Out.save()
    return feed_details(request)

  # context = {'update_feed': update_feed, 'update_feed': update_feed}

  return render(request, 'feed_s13_out_add.html', )


@login_required(login_url='/accounts/login')
def feed_s13_out_updaate(request, pk):
  update_feed_out = FeedS13_Outgoing.objects.get(id=pk)
  print(update_feed_out.date)
  print(update_feed_out.quantity)
  if request.method == 'POST':
    Date = request.POST.get("update_feed_out-date")
    Quantity = request.POST.get("feed-out-quantity")
    # sex = request.POST.get("gender")

    update_feed_out.date = Date
    update_feed_out.quantity = Quantity
    # update_feed.updated_by = request.user
    update_feed_out.save()

    return feed_details(request)

  context = {'update_feed_out': update_feed_out}

  return render(request, 'feed_s13_out_updaate.html', context)


@login_required(login_url='/accounts/login')
def feed_s13_out_delete(request, id):
  obj = get_object_or_404(FeedS13_Outgoing, id=id)
  obj.delete()
  return feed_details(request)


@login_required(login_url='/accounts/login')
def feeds16_in_add(request):
  FeedS16 = FeedS16_Incoming()

  if request.method == 'POST':
    Date = request.POST.get("feeds16-in-date")
    Quantity = request.POST.get("feeds16-in-quantity")
    Price = request.POST.get("feeds16-in-price")
    # sex = request.POST.get("gender")

    FeedS16.f16_date = Date
    FeedS16.f16_quantity = Quantity
    FeedS16.f16_price = Price
    FeedS16.f16_updated_by = request.user
    FeedS16.save()
    print(Quantity)
    print(Date)
    return feed_details(request)

  return render(request, 'feeds16_in_add.html')


@login_required(login_url='/accounts/login')
def feeds16_in_update(request, pk):
  FS16_in = FeedS16_Incoming.objects.get(id=pk)
  if request.method == 'POST':
    Date = request.POST.get("feeds16-in-date")
    Quantity = request.POST.get("feeds16-in-quantity")
    Price = request.POST.get("feeds16-in-price")
    FS16_in.f16_date = Date
    FS16_in.f16_quantity = Quantity
    FS16_in.f16_price = Price
    FS16_in.f16_updated_by = request.user
    FS16_in.save()
    return feed_details(request)
  context = {'FS16_in': FS16_in}

  return render(request, 'feeds16_in_update.html', context)


@login_required(login_url='/accounts/login')
def feeds16_in_delete(request, id):
  obj = get_object_or_404(FeedS16_Incoming, id=id)
  obj.delete()
  return feed_details(request)


@login_required(login_url='/accounts/login')
def feeds16_out_add(request, ):
  FeedS16_Out = FeedS16_Outgoing()

  if request.method == 'POST':
    Date = request.POST.get("feeds16-out-date")
    Quantity = request.POST.get("feeds16-out-quantity")
    Price = request.POST.get("feeds16-out-price")
    # sex = request.POST.get("gender")

    FeedS16_Out.f16_date = Date
    FeedS16_Out.f16_quantity = Quantity
    FeedS16_Out.f16_updated_by = request.user
    FeedS16_Out.save()
    print(Quantity)
    print(Date)
    return feed_details(request)

  return render(request, 'feeds16_out_add.html')


@login_required(login_url='/accounts/login')
def feeds16_out_update(request, pk):
  FeedS16_Out = FeedS16_Outgoing.objects.get(id=pk)
  if request.method == 'POST':
    Date = request.POST.get("feeds16-out-date")
    Quantity = request.POST.get("feeds16-out-quantity")
    # Price = request.POST.get("feeds16-out-price")
    FeedS16_Out.f16_date = Date
    FeedS16_Out.f16_quantity = Quantity
    # FeedS16_Out.f16_price = Price
    FeedS16_Out.f16_updated_by = request.user
    FeedS16_Out.save()
    return feed_details(request)
  context = {'FeedS16_Out': FeedS16_Out}
  return render(request, 'feeds16_out_update.html', context)


@login_required(login_url='/accounts/login')
def feeds16_out_delete(request, id):
  obj = get_object_or_404(FeedS16_Outgoing, id=id)
  obj.delete()
  return feed_details(request)
