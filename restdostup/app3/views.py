from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.
class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class ItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class ItemListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Логирование для анализа запросов
        if not request.user or not request.auth:
            raise PermissionDenied("You are not authorized to access this resource.")
        
        # Если пользователь авторизован, предоставляем данные
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)