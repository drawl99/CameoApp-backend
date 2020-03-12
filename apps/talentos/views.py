import json
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import UserSerializer, TalentSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .models import Talent
from django.http import Http404


# from .serializers import TalentSerializer


# class TalentViewSet(viewsets.ModelViewSet):
#     serializer_class = TalentSerializer
#     queryset = Talent.objects.all()

class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        user = self.get_object(username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = self.get_object(username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TalentList(APIView):

    def get(self, request):
        talents = Talent.objects.all()
        serializer = TalentSerializer(talents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TalentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TalentDetail(APIView):
    def get_object(self, username):
        try:
            user = User.objects.get(username=username)
            try:
                return Talent.objects.get(talent=user.id)
            except Talent.DoesNotExist:
                raise Http404
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        talent = self.get_object(username)
        serializer = TalentSerializer(talent)
        return Response(serializer.data)

    def put(self, request, username):
        talent = self.get_object(username)
        serializer = TalentSerializer(talent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        talent = self.get_object(username)
        talent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
