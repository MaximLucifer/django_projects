from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/minishop/images/', default='images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Делает модель абстрактной

class Clothing(Product):
    size = models.CharField(max_length=50)  # Размер
    material = models.CharField(max_length=100)  # Материал
    brand = models.CharField(max_length=100)  # Бренд

    def __str__(self):
        return f"{self.name} ({self.size})"

class Electronics(Product):
    brand = models.CharField(max_length=100)  # Бренд
    model_number = models.CharField(max_length=100)  # Номер модели
    warranty_period = models.IntegerField()  # Гарантия в месяцах

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model_number})"
    
class Automobile(Product):
    brand = models.CharField(max_length=100)  # Бренд автомобиля
    model_year = models.IntegerField()  # Год выпуска
    engine_type = models.CharField(max_length=50)  # Тип двигателя
    mileage = models.DecimalField(max_digits=10, decimal_places=2)  # Пробег

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model_year})"
    
class Jewelry(Product):
    material = models.CharField(max_length=100)  # Материал (золото, серебро и т.д.)
    weight = models.DecimalField(max_digits=10, decimal_places=2)  # Вес в граммах
    gemstone_type = models.CharField(max_length=100, blank=True, null=True)  # Тип камня (если есть)

    def __str__(self):
        return f"{self.name} ({self.material})"
    
class HomeAppliance(Product):
    energy_class = models.CharField(max_length=10)
    dimensions = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.energy_class})"