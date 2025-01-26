from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class Role(models.Model):
    name = models.CharField(_("Название роли"), max_length=50, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    code = models.CharField(_("Код"), max_length=50, blank=False)
    name = models.CharField(_("Название"), max_length=50, blank=False)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Car(models.Model):
    brand = models.CharField(_("Марка"), max_length=50, blank=False)
    model = models.CharField(_("Модель"), max_length=50, blank=False)
    year = models.IntegerField(
        _("Год выпуска"),
        validators=[MinValueValidator(1886), MaxValueValidator(9999)],
        blank=False
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class User(AbstractUser):
    name = models.CharField(_("Имя"), max_length=50, blank=False)
    surname = models.CharField(_("Фамилия"), max_length=50, blank=False)
    patronymic = models.CharField(_("Отчество"), max_length=50, blank=False)
    phone = models.CharField(_("Телефон"), max_length=17, blank=False)
    email = models.EmailField(_("Электронная почта"), max_length=50, unique=True, blank=False)
    drivers_license = models.CharField(_("Водительское удостоверение"), max_length=20, blank=False)
    role = models.ForeignKey(
        Role,
        verbose_name=_("Роль пользователя"),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.surname} {self.name} ({self.email})"


class Booking(models.Model):
    id_user = models.ForeignKey('User', verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    id_car = models.ForeignKey("Car", verbose_name=_("Автомобиль"), on_delete=models.CASCADE)
    id_status = models.ForeignKey("Status", verbose_name=_("Статус бронирования"), on_delete=models.CASCADE)
    booking_date = models.DateField(_("Дата бронирования"), blank=False)
    status_comment = models.TextField(_("Комментарий к статусу"), blank=True)

    def __str__(self):
        return f"Бронирование {self.id_car} для {self.id_user} на {self.booking_date}."
