from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import User


class RegisterForm(UserCreationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
                'type' : 'hidden',
            }))


    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

        widgets = {
            'first_name': forms.TextInput(attrs={'id':'first_name','placeholder':'First name', 'class': 'form-control', 'type' : 'hidden'}),
            'last_name': forms.TextInput(attrs={'id':'last_name','placeholder':'Last name', 'class': 'form-control', 'type' : 'hidden'}),
            'email': forms.EmailInput(attrs={'id':'email','placeholder':'Email Address', 'class': 'form-control', 'type' : 'hidden'}),
        }



class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    email = forms.CharField(
        widget = forms.EmailInput(
            attrs={
                'id': 'email',
                'placeholder': 'Email Address',
                'class': 'form-control'
            }))

    class Meta:
        model = User
        fields = ['email', 'password']




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



