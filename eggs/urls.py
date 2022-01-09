from django.urls import path
from . import views

app_name = "eggs"

urlpatterns = [
    path('records-details/', views.eggs_record_details, name="eggs_record_details"),
    path('add-egg-stock/', views.add_incoming_eggs, name="add_incoming_eggs"),
    path('update-incoming-stock/<id>/', views.update_incoming_stock, name="update_incoming_stock"),
    path('delete-incoming-stock/<id>/', views.delete_incoming_stock, name="delete_incoming_stock"),
    path('add-outgoing-egg-record/', views.add_outgoing_eggs, name="add_outgoing_eggs"),
    path('update-outgoing-egg-record/<id>/', views.update_outgoing_stock, name="update_outgoing_stock"),
    path('delete-outgoing-egg-record/<id>/', views.delete_outgoing_stock, name="delete_outgoing_stock"),

    path('generate_egg_slip/', views.generate_egg_slip, name="generate_egg_slip"),
]
