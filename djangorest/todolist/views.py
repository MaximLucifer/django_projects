from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task

# Create your views here.
class TaskCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailsView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
