from django.contrib import admin
from django.urls import path, include
from .import views
from django.urls import path

app_name = 'feed'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('feed_details/', views.feed_details, name='feed_details'),

    path('feed_add/', views.feed_add, name='feed_add'),
    path('feed_update/<str:pk>/', views.feed_update, name='feed_update'),
    path('Feed_delete/<id>/', views.Feed_delete, name='Feed_delete'),

    path('feed_s13_out_add/', views.feed_s13_out_add, name='feed_s13_out_add'),
    path('feed_s13_out_updaate/<str:pk>/', views.feed_s13_out_updaate, name='feed_s13_out_updaate'),
    path('feed_s13_out_delete/<id>/', views.feed_s13_out_delete, name='feed_s13_out_delete'),

    path('feeds16_in_add/', views.feeds16_in_add, name='feeds16_in_add'),
    path('feeds16_in_update/<str:pk>/', views.feeds16_in_update, name='feeds16_in_update'),
    path('feeds16_in_delete/<id>/', views.feeds16_in_delete, name='feeds16_in_delete'),

    path('feeds16_out_add/', views.feeds16_out_add, name='feeds16_out_add'),
    path('feeds16_out_update/<str:pk>/', views.feeds16_out_update, name='feeds16_out_update'),
    path('feeds16_out_delete/<id>/', views.feeds16_out_delete, name='feeds16_out_delete'),

    path('generate_feed_slip/', views.generate_feed_slip, name="generate_feed_slip"),
    # path('view_feed_slip/', views.view_feed_slip, name="view_feed_slip"),

]