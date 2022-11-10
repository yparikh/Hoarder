from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HoarderSerializer
from .models import Post

# Create your views here.
class HoarderView(viewsets.ModelViewSet):
    serializer_class = HoarderSerializer
    queryset = Post.objects.all()
