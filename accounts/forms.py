from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import User


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password1',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password2',
                'class' : 'form-control',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id':'username',
                'placeholder' : 'Username',
                'class' : 'form-control',
            }))

    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id':'first_name',
                'placeholder' : 'First name',
                'class' : 'form-control',
            }))

    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id':'last_name',
                'placeholder' : 'Last name',
                'class' : 'form-control',
            }))

    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                'id':'email',
                'placeholder' : 'Email Address',
                'class' : 'form-control',
            }))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')




class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'username',
                'placeholder': 'Username',
                'class': 'form-control'
            }))

    class Meta:
        model = User
        fields = ['username', 'password']




class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
        })
    )

class ResetPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
             }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password again',
                'class' : 'form-control',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )



