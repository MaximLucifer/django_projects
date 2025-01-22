from django.contrib import admin
from .models import Category, Role, Department, Status, Task, User

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name']

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id','code','name')
    search_fields = ['code','name']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','code','name')
    search_fields = ['code','name']
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','id_status','id_category','id_user')
    list_filter = ('id_status','id_category')
    search_fields = ['id_status']

@admin.register(User)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','id_role','id_department','email', 'full_name','phone')
    list_filter = ('id_role','id_department')
    search_fields = ['email','full_name','phone']