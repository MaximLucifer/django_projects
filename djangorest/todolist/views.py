from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied, NotFound
from .models import Task, Tasklist, Tag
from .serializers import TaskSerializer, TasklistSerializer, TagSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TasklistCreateView(generics.ListCreateAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tasklist.objects.filter(owner=self.request.user) 

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 

class TasklistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasklist.objects.all()
    serializer_class = TasklistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tasklist.objects.filter(owner=self.request.user) 

    def perform_update(self, serializer):
        if self.get_object().owner != self.request.user:
            raise PermissionDenied("Вы не можете редактировать этот список задач.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Вы не можете удалить этот список задач.")
        instance.delete()

class TaskCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        list_id = self.kwargs.get('list_id', None)
        return Task.objects.filter(tasklist__id=list_id, tasklist__owner=self.request.user) 

    def perform_create(self, serializer):
        list_id = self.kwargs.get('list_id', None)
        try:
            tasklist = Tasklist.objects.get(pk=list_id, owner=self.request.user) 
        except Tasklist.DoesNotExist:
            raise NotFound("Список задач не найден или у вас нет доступа.")
        serializer.save(tasklist=tasklist)

class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        list_id = self.kwargs.get('list_id', None)
        return Task.objects.filter(tasklist__id=list_id, tasklist__owner=self.request.user)  
