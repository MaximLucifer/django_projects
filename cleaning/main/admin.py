from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'address', 'created_at')
    search_fields = ('user__username', 'address')
    list_filter = ('date', 'time', 'created_at')