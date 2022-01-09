from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import  User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm

def logout_page(request):
  logout(request)
  return redirect('accounts:login')

  # return HttpResponse('<h1>Hello HttpResponse</h1>')


def login_page(request):
  if request.user.is_authenticated:
    return redirect('feed:dashboard')
  else:
    if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        # log the user in
        user = form.get_user()
        print(user)
        login(request, user)

        if 'next' in request.POST:
          return redirect(request.POST.get('next'))
        return redirect('feed:feed_details')
    else:
      form = AuthenticationForm()

  return render(request, 'login_page.html')

  # return HttpResponse('<h1>Hello HttpResponse</h1>')


def register_page(request):
  if request.user.is_authenticated:
    return redirect('feed:dashboard')
  else:
    form = CreateUserForm()

    if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')

        messages.success(request, 'Account Created For ' + username)
        return redirect('accounts:login')

  context = {'form': form}
    # if request.method == 'POST':
  #     Username = request.POST.get("username")
  #     Email = request.POST.get("email")
  #     Password1 = request.POST.get("password1")
  #     Password2 = request.POST.get("password2")
  #
  #
  #     if Password1 == Password2:
  #       if User.objects.filter(username=Username).exists():
  #         messages.info(request,"Username Already Exits")
  #         return redirect('accounts:register')
  #       elif User.objects.filter(email=Email).exists():
  #         messages.info(request,"Email is Already Exits")
  #         return redirect('accounts:register')
  #       else:
  #         user = User.objects.create_user(username=Username,password=Password1,email=Email)
  #         user.save()
  #         ss  =user.username
  #         messages.success(request, 'Account was Successfully Created For '+ ss )
  #
  #     else:
  #       messages.info(request,"Passwords Not Matching")
  #       return  redirect('accounts:register')
  #     return redirect('accounts:login')
  return render(request, 'register_page2.html',context)

# return HttpResponse('<h1>Hello HttpRespon/se</h1>')

# def logout_page(request):
#     # return redirect('dashboard:dashboard_view')
#     # logout(request)
#     # return login(request)
#     # return redirect('logout/')
#
