from django.shortcuts import render
from accounts.models import User
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from accounts.forms import RegisterForm, LoginForm, ResetPasswordForm, ResetPasswordConfirmForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register_page.html'
    success_url = reverse_lazy('accounts:login')


class MainLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login_page.html'


class ForgetPasswordView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'forget_password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'


class ResetPasswordView(PasswordResetConfirmView):
    form_class = ResetPasswordConfirmForm
    template_name= "password_reset_confirm.html" 
    success_url = reverse_lazy('accounts:login')
  


