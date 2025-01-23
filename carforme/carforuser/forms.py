import email
from enum import unique
from wsgiref import validate
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Role, User, Status, Car, Booking

class RegistrationForm(UserCreationForm):
    name = forms.CharField(
        label=_('Введите имя'),
        max_length=50,
        required=True
    )
    surname = forms.CharField(
        label=_('Введите фамилию'),
        max_length=50,
        required=True
    )
    patronymic = forms.CharField(
        label=_('Введите фамилию'),
        max_length=50,
        required=True
    )
    phone = forms.CharField(
        label=_('Введите номер телефона'),
        max_length=17,
        required=True
    )
    email = forms.EmailField(
        label=_('Введите адрес электронной почты'),
        required=True,
        unique=True
    )
    drivers_license = forms.CharField(
        label=_('Введите номер вашего водительского удостоверения'),
        max_length=20,
        required=True
    )
        
    class Meta:
        model = User
        fields = ['name', 'surname', 'patronymic', 'email','phone', 'drivers_license','password1','password2']
        labels = {
            'name': _('Имя'),
            'surname': _('Фамилия'),
            'patronymic': _('Отчество'),
            'phone': _('Номер телефона'),
            'drivers_license': _('Номер водительского удостоверения'),
            'email': _('Адрес электронной почты')
        }
        help_texts = {
            'password1': _('Введите надёжный пароль'),
            'password2': _('Повторите пароль'),
        }
    
    def clean_email(self):
        email = email.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationErr(_('Этот адрес электронной почты уже используется'))
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.patronymic = self.cleaned_data['patronymic']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        user.drivers_license = self.cleaned_data['drivers_license']
        if commit:
            user.save()
        return user

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        required=True,
        widget=forms.EmailInput(attrs={'autofocus': True})
        )
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['id_car', 'booking_date','status_comment']
        labels = {
            'id_car': _('Автомобиль'),
            'booking_date': _('Дата бронирования'),
            'status_comment': _('Комментарий к состоянию машины')
        }
        widgets = {
            'id_car': forms.Select(),
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'status_comment': forms.Textarea(attrs={'rows': 4})
        }