import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order_table(models.Model):
    id_user = models.ForeignKey('User_table', verbose_name=_('Пользователь'), on_delete=models.CASCADE, related_name='orders_with_users')
    id_product = models.ForeignKey('Product', verbose_name=_('Номер товара'), on_delete=models.CASCADE)
    id_status = models.ForeignKey('Status', verbose_name=_('Статус заказа'), on_delete=models.CASCADE, related_name='orders_with_statuses')
    quantity = models.IntegerField(verbose_name=_('Количество'), blank=False)
    delivery_address = models.CharField(verbose_name=_('Адрес доставки'), max_length=200, blank=False)
    order_date = models.DateTimeField(_('Время заказа'), auto_now_add=True)

    def __str__(self):
        return f'Заказ {self.id} - {self.quantity} - {self.delivery_address[:20]} - {self.order_date}'

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(_('Описание товара'))
    image = models.ImageField(_('Изображение товара'), upload_to='products/', blank=True, null=True, default='empty.txt')

    def __str__(self):
        return f'{self.name} | {self.price}'
    
class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Роль'), blank=False)

    def __str__(self):
        return self.name
    
class Status(models.Model):
    code = models.CharField(verbose_name=_('Код статуса'), max_length=50, blank=False)
    name = models.CharField(verbose_name=_('Статус'), max_length=50, blank=False)

    def __str__(self):
        return self.name
    
class User_table(AbstractUser):
    name = models.CharField(verbose_name=_('Имя'), max_length=50, blank=False)
    surname = models.CharField(verbose_name=_('Фамилия'), max_length=50, blank=False)
    patronymic = models.CharField(verbose_name=_('Отчество'), max_length=50, blank=False)
    phone = models.CharField(verbose_name=_('Номер телефона'), max_length=17, blank=False)
    id_role = models.ForeignKey('Role', verbose_name='Роль', on_delete=models.CASCADE, default='1')

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