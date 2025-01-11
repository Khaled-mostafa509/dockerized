from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password']


class OTPForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['OTP']


# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password']
# authentication/forms.py

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)
