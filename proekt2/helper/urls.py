from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('register/', views.register, name='register'),
    path('login/', views.CustomEmailLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('support_dashboard/', views.support_dashboard, name='dashboard'),
    path('support_dashboard/create_request/', views.create_request, name='create_request'),
    path('support_dashboard/admin_panel/', views.admin_panel, name='admin_panel'),
]