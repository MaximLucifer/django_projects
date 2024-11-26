# Generated by Django 5.1.3 on 2024-11-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minishop', '0005_remove_automobile_image_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeAppliance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='images/default.jpg', upload_to='static/minishop/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('energy_class', models.CharField(max_length=10)),
                ('dimensions', models.CharField(max_length=50)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
