import bleach
from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from .models import Booking

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(validators=[
        RegexValidator(
            regex=r'^[a-zA-Z0-9_]+$',
            message='Логин может содержать только буквы, цифры и символ "_"'
        )
    ])
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return bleach.clean(username, tags=[], attributes={})

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        return bleach.clean(first_name, tags=[], attributes={})

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        return bleach.clean(last_name, tags=[], attributes={})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return bleach.clean(email, tags=[], attributes={})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Хэшируем пароль
        if commit:
            user.save()
        return user

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'address', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'address': forms.TextInput(attrs={'placeholder': 'Введите адрес'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Дополнительные комментарии', 'rows': 3}),
        }

    def clean_address(self):
        address = self.cleaned_data.get('address', '')
        # Очищаем данные от любых HTML-тегов и оставляем только текст
        cleaned_address = bleach.clean(address, tags=[], attributes={}, strip=True)
        return cleaned_address

    def clean_comment(self):
        comment = self.cleaned_data.get('comment', '')
        # Если поле заполнено, очищаем его
        if comment:
            cleaned_comment = bleach.clean(comment, tags=[], attributes={}, strip=True)
            return cleaned_comment
        return comment

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            return bleach.clean(str(time), tags=[], attributes={}, strip=True)
        return time