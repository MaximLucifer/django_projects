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
    id_user = models.ForeignKey('User', on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    id_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    description = models.TextField(null=False)

    def __str__(self):
        return f'Task {self.id} - {self.description[:20]}'

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    id_role = models.ForeignKey(Role, on_delete=models.CASCADE, null=False, default='2')
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    full_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)

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