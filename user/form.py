from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('email', 'phone_number', 'username')


class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())