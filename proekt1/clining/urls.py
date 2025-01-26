from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_request', views.create_request, name='create_request'),
    path('admin_panel', views.admin_panel, name='admin_panel'),
    path('logout', views.logout_view, name='logout'),
]
    
