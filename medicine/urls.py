from django.contrib import admin
from django.urls import path, include
from .import views
from django.urls import path

app_name = 'medicine'

urlpatterns = [
    path('medicine_list', views.medicine_list, name='medicine_list'),

    path('medicine_add/', views.medicine_add, name='medicine_add'),
    path('medicine_update/<str:pk>/', views.medicine_update, name='medicine_update'),
    path('medicine_delete/<id>/', views.medicine_delete, name='medicine_delete'),

    path('generate_medicine_slip/', views.generate_medicine_slip, name="generate_medicine_slip"),

]