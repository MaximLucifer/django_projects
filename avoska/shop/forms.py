from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import User_table, Status, Product, Order_table

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        label=_('Логин')
        )
    name = forms.CharField(
        max_length=255,
        required=True,
        label=_('Имя')
        )
    surname = forms.CharField(
        max_length=50,
        required=True,
        label=_('Фамилия')
        )
    patronymic = forms.CharField(
        max_length=50,
        required=False,
        label=_('Отчество')
        )
    phone = forms.CharField(
        max_length=50,
        required=True,
        label=_('Номер телефона')
        )
    email = forms.CharField(
        max_length=17,
        required=True,
        label=_('Адрес электронной почты')
        )
    
    class Meta:
        model = User_table
        fields = ['username','name','surname','patronymic', 'email', 'password1', 'password2' ,'phone']
        labels = {
            'username': _('Логин'),
            'email': _('Адрес электронной почты'),
            'password1': _('Пароль'),
            'password2': _('Подтвердите пароль')
        }
        
    def save(self, commit = True):
        user = super().save(commit=False)
        user.name = self.cleaned_data['name']
        user.surname = self.cleaned_data['surname']
        user.patronymic = self.cleaned_data['patronymic']
        user.phone = self.cleaned_data['phone'] 
        if commit:
            user.save()
        return user
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order_table
        fields = ['id_product','quantity','delivery_address']
        labels = {
            'id_product': _('Выберите товар'),
            'quantity': _('Количество'),
            'delivery_address': _('Адрес доставки')
        }
        widgets = {
            'id_product': forms.Select(),
        }