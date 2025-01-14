from django.urls import path
from . import views

app_name = 'module1'

urlpatterns = [
    path('register/', views.register, name='module1_register'),
    path('login/', views.login_view, name='module1_login'),
    path('dashboard/', views.dashboard, name='module1_dashboard'),
    path('create_request/', views.create_request, name='module1_create_request'),
    path('admin_panel/', views.admin_panel, name='module1_admin_panel'),
]
