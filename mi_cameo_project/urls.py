from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserClientViewSet


# from apps.talentos.views import TalentViewSet



# router.register(r'talents',TalentViewSet)

# urlpatterns = router.urls

urlpatterns = [
    
    path('usuarios/',include('apps.usuarios.urls')),
    path('talentos/',include('apps.talentos.urls')),
    path('cameos/',include('apps.cameos.urls')),
    path('admin/', admin.site.urls),
    
    
    
    
    
    
    # path('api/', include('rest_framework.urls'), name= 'rest_framework'),
]
