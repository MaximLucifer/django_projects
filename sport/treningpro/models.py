from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey("User", verbose_name=_("ID пользователя"), on_delete=models.CASCADE)
    training_type = models.ForeignKey("Training_type", verbose_name=_("Тип тренировки"), on_delete=models.CASCADE)
    payment_method = models.ForeignKey("Payment_method", verbose_name=_("Способ оплаты"), on_delete=models.CASCADE)
    booking_status = models.ForeignKey("Booking_status", verbose_name=_("Статус"), on_delete=models.CASCADE)
    training_date = models.DateTimeField(_("Дата и время тренировки"), auto_now=False, auto_now_add=False)
    participants_count = models.IntegerField(_("Количество людей"))
    cancellation_reason = models.TextField(_("Причина отмены"))
    created_at = models.DateTimeField(_("Бронирование создано"), auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_id} - {self.training_type} - {self.payment_method} - {self.booking_status} - {self.training_date} - {self.participants_count} - {self.cancellation_reason} - {self.created_at}"
    
class Booking_status(models.Model):
    code = models.CharField(_("Код"), max_length=50)
    name = models.CharField(_("Название"), max_length=255)
    
    def __str__(self):
        return self.name
    
class Payment_method(models.Model):
    name = models.CharField(_("Название"), max_length=255)
    
    def __str__(self):
        return self.name

class Role(models.Model):
    code = models.CharField(_("Код"), max_length=50)
    name = models.CharField(_("Название"), max_length=255)
    
    def __str__(self):
        return self.name

class Training_type(models.Model):
    name = models.CharField(_("Название"), max_length=255)
    description = models.TextField(_("Описание"))
    

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    full_name = models.CharField(_("Полное имя"), max_length=255)
    phone = models.CharField(_("Номер телефона"), max_length=20)
    registration_date = models.DateTimeField(_("Дата регистрации"), auto_now=False, auto_now_add=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='User_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name='user_permissions',
        blank=True
        )
    
class User_role(models.Model):
    user_id = models.ForeignKey("User", verbose_name=_("Пользователь"), on_delete=models.CASCADE, default='1')
    role_id = models.ForeignKey("Role", verbose_name=_("ID роли"), on_delete=models.CASCADE)