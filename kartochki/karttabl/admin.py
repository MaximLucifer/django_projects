from django.contrib import admin
from .models import Clothes, Electronics, Car, Jewelry, HomeAppliance

# Register your models here.
@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'color', 'material')
    search_fields = ('title', 'description')

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'model_number')
    search_fields = ('title', 'description')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'model_year')
    search_fields = ('title', 'description')

@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'material', 'gemstone_type')
    search_fields = ('title', 'description')

@admin.register(HomeAppliance)
class HomeApplianceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'brand', 'model_number')
    search_fields = ('title', 'description')