from rest_framework import serializers
from .models import Talent, Category, Ocasion, Cameo, Comment, Review
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'email']


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
