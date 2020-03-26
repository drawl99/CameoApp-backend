from django.urls import path
from .views import TalentList, TalentDetail, ClientDetail, ClientList
from .api import activate, CustomTokenObtainPairView, RegisterUser

from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = 'usuarios'

urlpatterns = [
    path('api/1.0/register', RegisterUser.as_view(), name='register'),
    path('api/1.0/login', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/1.0/talents/', TalentList.as_view()),
    path('api/1.0/talents/<talent_id>/', TalentDetail.as_view()),
    path('api/1.0/clients/', ClientList.as_view()),
    path('api/1.0/clients/<client_id>/', ClientDetail.as_view()),
    path('api/1.0/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/1.0/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('activate/<slug:uidb64>/<slug:token>', activate, name='activate')
]