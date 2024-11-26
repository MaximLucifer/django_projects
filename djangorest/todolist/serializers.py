from rest_framework import serializers
from .models import Task, Tasklist, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True) 
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Tag.objects.all(), write_only=True, source='tags'  
    )

    class Meta:
        model = Task
        fields = [
            'id', 'name', 'description', 'completed', 'date_created',
            'date_modified', 'due_date', 'priority', 'tags', 'tag_ids', 'tasklist'
        ]

class TasklistSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)  
    owner = serializers.ReadOnlyField(source='owner.username')  

    class Meta:
        model = Tasklist
        fields = ['id', 'name', 'owner', 'tasks']
