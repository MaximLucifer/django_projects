from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        help_text="Пароль должен содержать не менее 8 символов, включая буквы, цифры и специальные символы."
    )
    agreement = forms.BooleanField(
        required=True,
        label="Согласие на обработку персональных данных"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Хэшируем пароль
        if commit:
            user.save()
        return user

class BookingForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    address = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea, required=False)
