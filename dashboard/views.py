from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required(login_url='/accounts/login')
def dashboard(request):
    return render(request, 'dashboard/homepage.html')
