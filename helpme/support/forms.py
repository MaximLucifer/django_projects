from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import Client, Task, Category, Status, Department

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255,
        required=True,
        label=_('Фамилия, Имя, Отчество'),
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        label=_('Номер телефона, с +7'),
    )
    email = forms.EmailField(
        required=True,
        label=_('Адрес электронной почты'),
    )
    id_department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        label=_('Отдел'),
        empty_label="Выберите отдел"
    )

    class Meta:
        model = Client
        fields = ['email', 'phone', 'password1', 'password2', 'id_department']
        labels = {
            'email': _('Адрес электронной почты'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
    
class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        required=True,
        widget=forms.EmailInput(attrs={'autofocus': True})
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id_category', 'id_status', 'description']
        labels = {
            'id_category': _('Категория запроса'),
            'id_status': _('Статус запроса'),
            'description': _('Опишите вашу проблему'),
        }
        widgets = {
            'id_category': forms.Select(),
            'id_status': forms.Select(),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
