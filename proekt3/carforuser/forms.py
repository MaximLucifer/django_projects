from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Status, User, Car, Booking

class RegistrationForm(UserCreationForm):
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
        max_length=17,
        required=True,
        label=_('Адрес электронной почты')
    )
    drivers_license = forms.CharField(
        max_length=20,
        required=True,
        label=_('Номер водительского удостоверения')
    )
    
    class Meta:
        model = User
        fields = ['name','surname', 'patronymic', 'email', 'password1', 'password2','phone','drivers_license']
        labels = {
            'email': _('Адрес электронной почты'),
            'password1': _('Пароль'),
            'password2': _('Подтвердите пароль')
        }

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            user.name = self.cleaned_data['name']
            user.surname = self.cleaned_data['surname']
            user.patronymic = self.cleaned_data['patronymic']
            user.phone = self.cleaned_data['phone']
            user.drivers_license = self.cleaned_data['drivers_license']
            if commit:
                user.save()
            return user
        
class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        required=True,
        widget=forms.EmailInput(attrs={'autofocus':True})
    )

class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_('Логин'),
        max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['id_car','booking_date','status_comment']
        widgets = {
            'id_car': forms.Select(),
            'booking_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%d-%m-%Y',
                ),
            'status_comment': forms.Textarea(attrs={'rows':4})
        }