from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Status, User, Category, Department, Task

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(
        max_length=255,
        required=True,
        label=_('Фамилия, имя, Отчество'),
    )
    phone = forms.CharField(
        max_length=255,
        required=True,
        label=_('Номер телефона'),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        label=_('Адрес электронной почты')
    )
    id_department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        label=_('Отдел'),
        empty_label=_('Выберите отдел'),
    )

    class Meta:
        model = User
        fields = ['email','phone','password1','password2','id_department']
        labels = {
            'email': _('Адрес электронной почты'),
            'password1': _('Пароль'),
            'password2': _('Подтвердите пароль'),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
    
class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Адрес электронной почты'),
        required=True,
        widget=forms.EmailInput(attrs={'autofocus':True})
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['id_category','description']
        labels = {
            'id_category': _('Категория вопроса'),
            'description': _('Опишите вашу проблему'),
        }
        widgets = {
            'id_category': forms.Select(),
            'description': forms.Textarea(attrs={'rows': 4})
        }