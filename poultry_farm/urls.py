from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eggs/', include('eggs.urls')),
    path('birds/', include('birds.urls')),
    path('employee/', include('employee.urls')),
    path('feed/', include('feed.urls')),
    path('medicine/', include('medicine.urls')),
    path('accounts/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('expenses/', include('expenses.urls')),
    path('', views.homepage, name="homepage"),

    path('accounts/', include('django.contrib.auth.urls'))

]
