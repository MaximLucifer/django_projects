from django.urls import path
from .views import (
    TagListCreateView, TasklistCreateView, TasklistDetailsView,
    TaskCreateView, TaskDetailsView
)

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tags'),
    path('', TasklistCreateView.as_view(), name='tasklists'),
    path('todolists/<int:pk>/', TasklistDetailsView.as_view(), name='tasklist-detail'),
    path('todolists/<int:list_id>/tasks/', TaskCreateView.as_view(), name='tasks'),
    path('todolists/<int:list_id>/tasks/<int:pk>/', TaskDetailsView.as_view(), name='task-detail'),
]
