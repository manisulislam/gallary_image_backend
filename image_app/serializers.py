from rest_framework import serializers
from .models import ImageBox

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBox
        fields = '__all__'