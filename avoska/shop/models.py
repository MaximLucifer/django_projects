import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order_table(models.Model):
    id_user = models.ForeignKey("User_table", verbose_name=_("Пользователь"), on_delete=models.CASCADE)
    id_product = models.ForeignKey("Product", verbose_name=_("Номер товара"), on_delete=models.CASCADE)
    id_status = models.ForeignKey("Status", verbose_name=_("Статус заказа"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("Количество"), blank=False)
    delivery_address = models.CharField(_("Адрес доставки"), max_length=200, blank=False)
    order_date = models.DateTimeField(_("Время заказа"), auto_now_add=True)
    
    def __str__(self):
        return f'Заказ {self.id} - {self.quantity} - {self.delivery_address[:20]} - {self.order_date}'
    
class Product(models.Model):
    name = models.CharField(_("Название"), max_length=100, blank=False)
    price = models.DecimalField(_("Цена"), max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(_("Описание"))
    
    def __str__(self):
        return f'{self.name} - {self.price} - {self.description[:20]}'
    
class Role(models.Model):
    name = models.CharField(_("Название"), max_length=50, blank=False)
    
    def __str__(self):
        return self.name
    
class Status(models.Model):
    code = models.CharField(_("Код"), max_length=50, blank=False)
    name = models.CharField(_("Название"), max_length=50, blank=False)
    
    def __str__(self):
        return self.name
    
class User_table(AbstractUser):
    name = models.CharField(_("Имя"), max_length=50)
    surname = models.CharField(_("Фамилия"), max_length=50)
    patronymic = models.CharField(_("Отчество"), max_length=50)
    phone = models.CharField(_("Номер телефона"), max_length=50)
    id_role = models.ForeignKey("Role", verbose_name=_("Роль"), on_delete=models.CASCADE, default='1')
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='User_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='User_permissions',
        blank=True
    )