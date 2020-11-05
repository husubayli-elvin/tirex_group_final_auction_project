from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView, ResetPasswordView, ResetPasswordConfirmView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name = 'password-reset-confirm'),

]