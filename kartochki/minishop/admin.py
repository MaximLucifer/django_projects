from django.contrib import admin
from .models import Clothing, Electronics, Automobile, HomeAppliance, Jewelry

# Register your models here.
@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'size')
    search_fields = ('name', 'description', 'brand')

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'model_number')
    search_fields = ('name', 'description', 'brand')

@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'model_year')
    search_fields = ('name', 'description', 'brand')

@admin.register(HomeAppliance)
class HomeApplianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'energy_class', 'dimensions')
    search_fields = ('name', 'description')

@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'material', 'weight')
    search_fields = ('name', 'description', 'material')