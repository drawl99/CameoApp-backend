
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserClientViewSet
from apps.talentos.views import TalentViewSet

router = DefaultRouter()
router.register(r'usuarios',UserClientViewSet)
router.register(r'talents',TalentViewSet)


#urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('api/', include('rest_framework.urls'), name= 'rest_framework'),
]
