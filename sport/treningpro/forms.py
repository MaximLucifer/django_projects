from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Training_type, Payment_method, Booking, User

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        label=_('Полное имя'), 
        max_length=255, 
        required=True)
    phone = forms.CharField(
        label=_('Номер телефона'),
        max_length=20,
        required=True)
    
    class Meta:
        model = User
        fields = ['username','password1','password2','email','full_name','phone']
        labels = {
            'username': _('Логин'),
            'email': _('Адрес электронной почты'),
            'password1': _('Введите пароль'),
            'password2': _('Подтвердите пароль')
        }
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.username = self.cleaned_data['username']
            user.phone = self.cleaned_data['phone']
            user.full_name = self.cleaned_data['full_name']
            if commit:
                user.save()
            return user
        
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['training_type', 'training_date','participants_count','payment_method']
        label = {
            'training_type': _('Вид тренировки'),
            'training_date': _('Дата тренировки'),
            'participants_count': _('Количество участников'),
            'payment_method': _('Способ оплаты'),
        }
        widgets = {
            'training_type': forms.Select(),
        }