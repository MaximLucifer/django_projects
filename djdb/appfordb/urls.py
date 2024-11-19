from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.base_view , name='home'),
    path('profile', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('news/', views.news_list, name='news_list'),
    path('news/category/<int:category_id>/', views.news_list, name='news_by_category'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:category_id>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
]
