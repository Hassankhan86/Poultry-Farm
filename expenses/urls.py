from django.urls import path, include
from . import views

app_name = "expense"

urlpatterns = [
    path('', views.expenses_view, name="expenses_view"),
    path('add-other-expenses/', views.add_expense, name="add_other_expenses" ),
    path('update-expenses/<id>/', views.update_expenses, name="update_expenses"),
    path('delete-expense/<id>/', views.delete_expense, name="delete_expenses"),
    path('generate-expense/', views.generated_expense, name="generated_expense"),

]
