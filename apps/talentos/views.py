from django.shortcuts import render
from rest_framework import viewsets
from .models import Talent
from .serializers import TalentSerializer

class TalentViewSet(viewsets.ModelViewSet):
    serializer_class = TalentSerializer
    queryset = Talent.objects.all()
    
