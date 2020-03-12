from django.shortcuts import render
from rest_framework import viewsets
from .models import UserClient
from .serializers import UserClientSerializer


class UserClientViewSet(viewsets.ModelViewSet):
    serializer_class = UserClientSerializer
    queryset = UserClient.objects.all()
