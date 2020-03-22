# from django.contrib.auth.models import User
from django.http import Http404
# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer


class UserClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ClientList(APIView):

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):

    def get_object(self, client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            raise Http404

    def get(self, request, client_id):
        client = self.get_object(client_id)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, client_id):
        client = self.get_object(client_id)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, client_id):
        client = self.get_object(client_id)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
