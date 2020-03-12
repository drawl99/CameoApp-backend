from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserClientViewSet
# from apps.talentos.views import TalentViewSet
from apps.talentos import views

router = DefaultRouter()
router.register(r'usuarios', UserClientViewSet)
# router.register(r'talents',TalentViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/1.0/users/', views.UserList.as_view()),
    path('api/1.0/users/<username>/', views.UserDetail.as_view()),
    path('api/1.0/talents/', views.TalentList.as_view()),
    path('api/1.0/talents/<username>/', views.TalentDetail.as_view()),
    # path('api/', include('rest_framework.urls'), name= 'rest_framework'),
]
