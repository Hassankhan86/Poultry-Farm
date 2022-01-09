from django.urls import path, include
from . import views

app_name = 'birds'


urlpatterns = [
    path('records/', views.birds_record_view, name="birds_record_view"),
    path('add-birds/', views.add_more_alive_birds, name="add-more-alive-bird"),
    path('update-alive-birds-record/<id>/', views.update_more_alive_birds, name="update_more_alive_birds"),
    path('delete-alive-birds-record/<id>/', views.delete_alive_birds_record, name="delete_alive_birds_record"),
    path('add-birds-death/', views.add_birds_deaths, name="add_birds_deaths"),
    path('update-birds-death-record/<id>/', views.update_birds_deaths, name="update_birds_deaths"),
    path('delete-dead-birds-record/<id>/', views.delete_dead_birds_record, name="delete_dead_birds_record"),

    path('generate_birds_slip/', views.generate_birds_slip, name="generate_birds_slip"),

]
