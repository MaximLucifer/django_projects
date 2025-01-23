from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .forms import _

# Create your models here.

class Booking(models.Model):
    id_user = models.ForeignKey('User', verbose_name=_(""), on_delete=models.CASCADE)
    id_car = models.ForeignKey("Car", verbose_name=_(""), on_delete=models.CASCADE)
    id_status = models.ForeignKey("Status", verbose_name=_(""), on_delete=models.CASCADE)
    booking_date = models.DateField(_("Дата бронирования"), blank=False)
    status_comment = models.TextField(_("Комментарий к статусу"), Blank=True)
    
    def __str__(self):
        return f"Бронирование {self.car} для {self.user} на {self.booking_date}."
    
class Car(models.Model):
    brand = models.CharField(_("Марка"), max_length=50, blank=False)
    model = models.CharField(_("Модель"), max_length=50, blank=False)
    year = models.IntegerField(
        _("Год выпуска"),
        validators=[MinValueValidator(1886), MaxValueValidator(9999)],
        blank=False)
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    code = models.CharField(_(""), max_length=50, blank=False)
    name = models.CharField(_(""), max_length=50, blank=False)
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
class User(AbstractUser):
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    patronymic = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=17, blank=False)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    drivers_license = models.CharField(max_length=20, blank=False)
    id_role = models.ForeignKey(
        Role, 
        verbose_name=_("Роль пользователя"),
        on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.surname} {self.name} ({self.email})"