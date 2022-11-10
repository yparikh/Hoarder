from rest_framework import serializers
from .models import Post

class HoarderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
