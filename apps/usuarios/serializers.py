from rest_framework import serializers
from .models import Client, Talent
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        # try:
        #     user_profile = UserProfile.objects.get(user=self.user)
        # except UserProfile.DoesNotExist:
        #     user_profile = None

        # if user_profile:
        #     data.update({'completed': True})
        # else:
        #     data.update({'completed': False})
      
        return data