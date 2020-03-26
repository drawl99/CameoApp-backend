from django.urls import path
from .views import CategoryList, CategoryDetail, ReviewList, ReviewDetail

urlpatterns = [
    path('api/1.0/categories/', CategoryList.as_view()),
    path('api/1.0/categories/<category_id>/', CategoryDetail.as_view()),
    path('api/1.0/reviews/',ReviewList.as_view()),
    path('api/1.0/reviews/<review_id>/', ReviewDetail.as_view()),
]