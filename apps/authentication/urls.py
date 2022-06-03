# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, PasswordsChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('change-password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password-reset/password_reset.html',
             subject_template_name='accounts/password-reset/password_reset_subject.txt',
             email_template_name='accounts/password-reset/password_reset_email.html',
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
