from django.contrib import admin
from django.urls import path, include
from .import views
from django.urls import path

app_name = 'employee'

urlpatterns = [
    path('employee_list', views.employee_list, name='employee_list'),

    path('employee_add/', views.employee_add, name='employee_add'),
    path('employee_update/<str:pk>/', views.employee_update, name='employee_update'),
    path('employee_delete/<id>/', views.employee_delete, name='employee_delete'),
    path('pay_salary/', views.pay_salary, name="pay_salary"),

    path('paid-salary-record/', views.paid_salary_record, name='paid_salary_record'),
    path('pay_salary/', views.pay_salary, name="pay_salary"),
    path('update-paid-salary/<id>/', views.update_salary_paid_record, name="update_salary_paid_record"),
    path('delete-paid-salary-record/<id>/', views.delete_salary_paid_record, name="delete_salary_paid_record"),

]