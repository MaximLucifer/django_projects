from django.contrib import admin
from .models import User, Booking, Booking_status, Payment_method, Role, Training_type, User_role

# Register your models here.

@admin.register(Booking_status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['code','name']
    search_fields = ['name']

@admin.register(User_role)
class User_roleAdmin(admin.ModelAdmin):
    list_display = ['user_id','role_id']

@admin.register(Payment_method)
class Payment_methodAdmin(admin.ModelAdmin):
    list_display = ['name']
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['code','name']
    search_fields = ['code', 'name']
    
@admin.register(Training_type)
class Training_typeAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','full_name', 'email','phone', 'registration_date']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user_id','training_type','payment_method','booking_status','training_date','participants_count','cancellation_reason','created_at']




