# Generated by Django 5.1.3 on 2024-11-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minishop', '0004_automobile_clothing_electronics_jewelry_delete_card_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='automobile',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='automobile',
            name='video_url',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='clothing',
            name='video_url',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='video_url',
        ),
        migrations.RemoveField(
            model_name='jewelry',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='jewelry',
            name='video_url',
        ),
        migrations.AddField(
            model_name='automobile',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='static/minishop/images/'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='static/minishop/images/'),
        ),
        migrations.AddField(
            model_name='electronics',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='static/minishop/images/'),
        ),
        migrations.AddField(
            model_name='jewelry',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='static/minishop/images/'),
        ),
    ]