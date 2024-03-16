# order_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Request


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['request_type', 'urgency']
