from django.shortcuts import render
from django.http import HttpResponse

from .models import Task, Client
from rest_framework import viewsets
from .serializers import TaskSerializer, ClientSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer