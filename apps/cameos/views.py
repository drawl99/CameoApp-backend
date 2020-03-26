from rest_framework.response import Response
from .serializers import CameoSerializer,CommentSerializer,OcasionSerializer
from rest_framework.views import APIView
from rest_framework import status
from .models import Cameo,Comment,Ocasion
from django.http import Http404


class OcasionList(APIView):

    def get(self, request):
        ocasions = Ocasion.objects.all()
        serializer = OcasionSerializer(ocasions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OcasionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OcasionDetail(APIView):

    def get_object(self, ocasion_id):
        try:
            return Ocasion.objects.get(id=ocasion_id)
        except Ocasion.DoesNotExist:
            raise Http404

    def get(self, request, ocasion_id):
        ocasion = self.get_object(ocasion_id)
        serializer = OcasionSerializer(ocasion)
        return Response(serializer.data)

    def put(self, request, ocasion_id):
        ocasion = self.get_object(ocasion_id)
        serializer = OcasionSerializer(ocasion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, ocasion_id):
        ocasion = self.get_object(ocasion_id)
        ocasion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CameoList(APIView):

    def get(self, request):
        cameos = Cameo.objects.all()
        serializer = CameoSerializer(cameos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CameoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CameoDetail(APIView):

    def get_object(self, cameo_id):
        try:
            return Cameo.objects.get(id=cameo_id)
        except Cameo.DoesNotExist:
            raise Http404

    def get(self, request, cameo_id):
        cameo = self.get_object(cameo_id)
        serializer = CameoSerializer(cameo)
        return Response(serializer.data)

    def put(self, request, cameo_id):
        cameo = self.get_object(cameo_id)
        serializer = CameoSerializer(cameo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, cameo_id):
        cameo = self.get_object(cameo_id)
        cameo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    def get_object(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment_id):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, comment_id):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

