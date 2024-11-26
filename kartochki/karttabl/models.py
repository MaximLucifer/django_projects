from django.db import models

# Create your models here.
class Clothes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=50)
    sizes = models.CharField(max_length=50)  # Например: "S, M, L"
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в рублях
    image = models.ImageField(upload_to='static/karttabl/clothes/', default='images/default.jpg')  # Поле для изображения

    def __str__(self):
        return self.title
    
class Electronics(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField()  # Например: "Процессор: Intel i7, Оперативная память: 16GB"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в рублях
    image = models.ImageField(upload_to='static/karttabl/electronics/', default='images/default.jpg')  # Поле для изображения

    def __str__(self):
        return self.title

class Car(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    model_year = models.PositiveIntegerField()  # Год выпуска
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в рублях
    image = models.ImageField(upload_to='static/karttabl/cars/', default='images/default.jpg')  # Поле для изображения

    def __str__(self):
        return f"{self.brand} {self.title} ({self.model_year})"

class Jewelry(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    material = models.CharField(max_length=100)  # Например: "Золото, Серебро"
    gemstone_type = models.CharField(max_length=100)  # Например: "Алмаз, Изумруд"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в рублях
    image = models.ImageField(upload_to='static/karttabl/jewelry/', default='images/default.jpg')  # Поле для изображения

    def __str__(self):
        return self.title

class HomeAppliance(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100)
    specifications = models.TextField()  # Например: "Мощность: 1500W, Объем: 1.5L"
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена в рублях
    image = models.ImageField(upload_to='static/karttabl/home_appliances/', default='images/default.jpg')  # Поле для изображения

    def __str__(self):
        return self.title