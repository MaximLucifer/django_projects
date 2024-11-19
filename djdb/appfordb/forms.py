from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, Category


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.widgets.DateInput(format='%d.%m.%Y', attrs={'placeholder': 'дд.мм.гггг'})
    )

    class Meta:
        model = Profile
        fields = ['date_of_birth']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    