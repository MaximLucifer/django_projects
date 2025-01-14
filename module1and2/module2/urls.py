from django.urls import path
from . import views

app_name = 'module2'

urlpatterns = [
    path('register/', views.register, name='module2_register'),
    path('login/', views.login_view, name='module2_login'),
    path('dashboard/', views.dashboard, name='module2_dashboard'),
    path('create_request/', views.create_request, name='module2_create_request'),
    path('admin_panel/', views.admin_panel, name='module2_admin_panel'),
]
