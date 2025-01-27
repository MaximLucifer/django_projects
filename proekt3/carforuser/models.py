from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Booking(models.Model):
    id_booking = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_car = models.ForeignKey('Car', on_delete=models.CASCADE)
    id_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    booking_date = models.DateField(blank=False)
    status_comment = models.TextField()

    def __str__(self):
        return f"Booking {self.id_booking} for {self.id_car.brand} {self.id_car.model}"  # Пример строки для возврата

class Car(models.Model):
    id_car = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=50, blank=False)
    model = models.CharField(max_length=50, blank=False)
    year = models.IntegerField(blank=False)
    registration_number = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    patronymic = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=17, blank=False, unique=True)
    drivers_license = models.CharField(max_length=20, blank=False)
    id_role = models.ForeignKey('Role', on_delete=models.CASCADE, default='1')

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

    def __str__(self):
        return f"{self.name} {self.surname}"