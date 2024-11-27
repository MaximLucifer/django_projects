from django.urls import path
from .views import fetch_items

urlpatterns = [
    path('fetch-items/', fetch_items, name='fetch-items'),
]