from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Client, CleaningRequest

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255,
        required=True,
        label=_('Фамилия, Имя, Отчество'),
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        label=_('Номер телефона'),
    )
    email = forms.EmailField(
        required=True,
        label=_('Адрес электронной почты')
    )
    
    class Meta:
        model = Client
        fields = ['username', 'password1', 'password2', 'full_name', 'phone', 'email']
        labels = {
            'username': _('Имя пользователя'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }
        
class RequestForm(forms.ModelForm):
    class Meta:
        model = CleaningRequest
        fields = ['address', 'contact_info', 'service_type', 'payment_type', 'date_time']
        labels = {
            'address': _('Адрес'),
            'contact_info': _('Контактная информация'),
            'service_type': _('Тип услуги'),
            'payment_type': _('Тип оплаты'),
            'date_time': _('Дата и время'),
        }