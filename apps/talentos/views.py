from rest_framework.response import Response
from .serializers import UserSerializer, TalentSerializer, CategorySerializer, OcasionSerializer, CameoSerializer, \
    CommentSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from .models import Talent, Category, Ocasion, Cameo, Comment, Review
from django.http import Http404


class CategoryList(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):

    def get_object(self, category_id):
        try:
            return Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        category = self.get_object(category_id)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = self.get_object(category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

    def get_object(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = self.get_object(user_id)
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

    def get_object(self, talent_id):
        try:
            return Talent.objects.get(id=talent_id)
        except Talent.DoesNotExist:
            raise Http404

    def get(self, request, talent_id):
        talent = self.get_object(talent_id)
        serializer = TalentSerializer(talent)
        return Response(serializer.data)

    def put(self, request, talent_id):
        talent = self.get_object(talent_id)
        serializer = TalentSerializer(talent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, talent_id):
        talent = self.get_object(talent_id)
        talent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ReviewList(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):

    def get_object(self, review_id):
        try:
            return Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, review_id):
        review = self.get_object(review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, review_id):
        review = self.get_object(review_id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = self.get_object(review_id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
