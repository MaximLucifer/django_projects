from django.contrib import admin
from .models import User, Booking, Car, Role, Status

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname','patronymic','phone','email','drivers_license','id_role']
    search_fields = ['']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = []
    search_fields = []

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_dispaly = ['id_car','brand','model','year','registration_number']
    search_fields = ['']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['code','name']
    search_fields = []