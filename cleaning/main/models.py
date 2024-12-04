import bleach
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Username is required")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[RegexValidator(r'^[a-zA-Z]+$')]
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Фильтруем данные перед сохранением
        self.address = bleach.clean(self.address, tags=[], attributes={})
        if self.comment:
            self.comment = bleach.clean(self.comment, tags=[], attributes={})
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time}"