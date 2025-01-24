from django.contrib import admin
from .models import User_table, Product, Status, Role, Order_table

# Register your models here.

@admin.register(Order_table)
class OrderTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'id_product', 'id_status', 'quantity', 'delivery_address', 'order_date')
    list_filter = ('id_status', 'order_date')
    search_fields = ('id_user__username', 'delivery_address')
    ordering = ('-order_date',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')
    search_fields = ('code', 'name')


@admin.register(User_table)
class UserTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'surname', 'patronymic', 'phone', 'email', 'id_role')
    list_filter = ('id_role', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'phone', 'name', 'surname')
    ordering = ('username',)