from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)
    
    def __str__(self):
        return self.name

class Department(models.Model):
    code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Role(models.Model):
    code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Status(models.Model):
    code = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    id_user = models.ForeignKey('Client', on_delete=models.CASCADE, null=False)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE, null=False)
    description = models.TextField()

    def __str__(self):
        return f'Task {self.id} - {self.description[:20]}'


class Client(AbstractUser):

    USERNAME_FIELD = 'email'
    
    id_role = models.ForeignKey(Role, default='2', on_delete=models.CASCADE, null=False)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    username = None
    full_name = models.CharField(max_length=55, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='Client_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='Client_permissions',
        blank=True
    )