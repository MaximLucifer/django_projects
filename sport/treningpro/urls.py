from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/create_request', views.create_request, name='create_request'),
    path('dashboard/admin_panel', views.admin_panel, name='admin_panel'),
]
