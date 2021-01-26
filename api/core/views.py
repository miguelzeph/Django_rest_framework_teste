from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

# ViewSets define the view behavior.
class cliente_view_set(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
