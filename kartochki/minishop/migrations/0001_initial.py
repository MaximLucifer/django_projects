# Generated by Django 5.1.3 on 2024-11-25 09:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('attributes', models.JSONField(default=dict, verbose_name='Характеристики')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='minishop.category', verbose_name='Категория')),
            ],
        ),
    ]