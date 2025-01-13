from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Request

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=15)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'phone', 'email']

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['address', 'contact_info', 'service_type', 'payment_type', 'date_time']

