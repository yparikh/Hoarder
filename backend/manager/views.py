from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ManagerSerializer
from .models import Manager

# Create your views here.

class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
