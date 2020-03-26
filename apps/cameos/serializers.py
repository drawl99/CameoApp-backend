from rest_framework import serializers
from .models import Cameo,Comment, Ocasion

class OcasionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocasion
        fields = '__all__'


class CameoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cameo
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
