from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Request(models.Model):
    SERVICE_CHOICES = [
        ('general', 'Общий клининг'),
        ('deep', 'Генеральная уборка'),
        ('post_construction', 'Послестроительная уборка'),
        ('carpet', 'Химчиста ковров и мебели'),
    ]
    PAYMENT_CHOICES = [
        ('cash', 'Наличные'),
        ('card', 'Банковская карта')
    ]
    STATUS_CHOICES = [
        ('new', 'Новая заявка'),
        ('process', 'В процессе'),
        ('completed', 'Услуга оказана'),
        ('cancelled', 'Услуга отменена')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact_info = models.TextField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    reason_for_cancellation = models.TextField(blank=True, null=True)