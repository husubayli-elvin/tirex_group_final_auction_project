from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, MainLoginView, ForgetPasswordView, ResetPasswordView
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', MainLoginView.as_view(), name='login'),
    path('log-out/', LogoutView.as_view(), name='log-out'),
    path('reset-password/', ForgetPasswordView.as_view(), name='reset-password'),
    path('password-reset-confirm/<str:uidb64>/<str:token>/', ResetPasswordView.as_view(), name = 'password-reset-confirm'),

]