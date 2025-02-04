from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomEmailLoginView.as_view(), name='login'),
    path('admin_panel/admin_login/', views.admin_login_view, name='admin_login'),
    path('logout/', views.logout_view, name='logout'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('dashboard/create_request/', views.create_request, name='create_request'),
    path('dashboard', views.booking_dashboard, name='dashboard'),
]