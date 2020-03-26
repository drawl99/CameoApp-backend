from django.urls import path
from .views import OcasionList,OcasionDetail, CameoList,CameoDetail, CommentList,CommentDetail

urlpatterns = [
    path('api/1.0/ocasions/', OcasionList.as_view()),
    path('api/1.0/ocasions/<ocasion_id>/', OcasionDetail.as_view()),
    path('api/1.0/cameos/', CameoList.as_view()),
    path('api/1.0/cameos/<cameo_id>/', CameoDetail.as_view()),
    path('api/1.0/comentarios/', CommentList.as_view()),
    path('api/1.0/comentarios/<comentario_id>/', CommentDetail.as_view()),
]