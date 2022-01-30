from django.contrib import admin
from django.urls import path, include
from .import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),

     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

    # path('reset_passwrd_comord_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_passwoplete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]


    # path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    # path('reset_passwrd_comord_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset_passwoplete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

