from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tasklist(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='tasklists', on_delete=models.CASCADE)  # Добавлено поле owner

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=True)
    completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    date_modified = models.DateField(auto_now=True)
    priority = models.CharField(
        max_length=1,
        choices=[('h', 'High'), ('m', 'Medium'), ('l', 'Low'), ('n', 'None')],
        default='n'
    )
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)  # Добавлена связь "многие ко многим"
    tasklist = models.ForeignKey(Tasklist, related_name='tasks', on_delete=models.CASCADE, default='1')

    def __str__(self):
        return self.name
