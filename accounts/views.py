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

class ProfileView(DetailView):
    model = User
    context_object_name = "profile"
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BuyingView(DetailView):
    model = User
    context_object_name = "buying"
    template_name = 'accounts_html/buying.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    
class CopListView(DetailView):
    model = User
    context_object_name = "coplist"
    template_name = 'accounts_html/cop-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PortfolioView(DetailView):
    model = User
    context_object_name = "portfolio"
    template_name = 'accounts_html/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SellingView(DetailView):
    model = User
    context_object_name = "selling"
    template_name = 'accounts_html/selling.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SettingView(DetailView):
    model = User
    context_object_name = "setting"
    template_name = 'accounts_html/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context