from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)       
    email = models.EmailField(unique=True)                    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='clining_user_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='clining_user_permissions',
        blank=True
    )
    
class CleaningRequest(models.Model):
    SERVICE_CHOICES = [
        ('Общий', 'Общий клининг'),
        ('Генеральная', 'Генеральная уборка'),
        ('Строительная', 'Послестроительная уборка'),
        ('Химчистка', 'Химчистка ковров и мебели'),
    ]
    PAYMENT_CHOICES = [
        ('Наличные', 'Наличные'),
        ('Банковская карта', 'Банковская карта'),
    ]
    STATUS_CHOICES = [
        ('Новая', 'Новая заявка'),
        ('В процессе', 'В процессе выполнения'),
        ('Выполнено', 'Услуга оказана'),
        ('Отменено', 'Услуга отменена'),
    ]
    
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact_info = models.TextField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    reason_for_cancellation = models.TextField(blank=True, null=True)
