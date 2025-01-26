from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now
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
        label=_('Введите отчество'),
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
        email = self.cleaned_data.get('email')  # Достаем email из cleaned_data
        if email and User.objects.filter(email=email).exists():
            raise ValidationError(_('Этот адрес электронной почты уже используется.'))
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
    booking_date = forms.DateField(
        label="Дата бронирования",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Booking
        fields = ['id_car', 'booking_date', 'status_comment']
        labels = {
            'id_car': 'Автомобиль',
            'booking_date': 'Дата бронирования',
            'status_comment': 'Комментарий к бронированию',
        }

    def clean_booking_date(self):
        booking_date = self.cleaned_data['booking_date']
        if booking_date < now().date():
            raise ValidationError("Дата бронирования не может быть в прошлом.")
        return booking_date