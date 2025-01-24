from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Role, Status, Order_table, User_table, Product

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        label=_('Логин')
    )
    name = forms.CharField(
        max_length=50,
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
        required=True,
        label=_('Отчество')
    )
    phone = forms.CharField(
        max_length=50,
        required=True,
        label=_('Номер телефона')
    )
    email = forms.EmailField(
        required=True,
        label=_('Адрес электронный почты')
    )

    class Meta:
        model = User_table
        fields = ['username', 'email', 'password1', 'password2', 'name','surname','patronymic','phone']
        labels = {
            'username': _('Логин'),
            'email': _('Адрес электронной почты'),
            'password1': _('Введите пароль'),
            'password2': _('Подтвердите пароль')
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
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
        fields = ['id_product','quantity', 'delivery_address']
        labels = {
            'id_product': _('Выберите товар'),
            'quantity': _('Выберите количество'),
            'delivery_address': _('Адрес доставки')
        }
        widgets = {
            'id_product': forms.Select(),
        }