from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.usuarios.views import UserClientViewSet
# from apps.talentos.views import TalentViewSet
from apps.talentos import views as talentos_views
from apps.usuarios import views as usuarios_views

router = DefaultRouter()
router.register(r'usuarios', UserClientViewSet)
# router.register(r'talents',TalentViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/1.0/users/', talentos_views.UserList.as_view()),
    path('api/1.0/users/<user_id>/', talentos_views.UserDetail.as_view()),
    path('api/1.0/talents/', talentos_views.TalentList.as_view()),
    path('api/1.0/talents/<talent_id>/', talentos_views.TalentDetail.as_view()),
    path('api/1.0/categories/', talentos_views.CategoryList.as_view()),
    path('api/1.0/categories/<category_id>/', talentos_views.CategoryDetail.as_view()),
    path('api/1.0/ocasions/', talentos_views.OcasionList.as_view()),
    path('api/1.0/ocasions/<ocasion_id>/', talentos_views.OcasionDetail.as_view()),
    path('api/1.0/cameos/', talentos_views.CameoList.as_view()),
    path('api/1.0/cameos/<cameo_id>/', talentos_views.CameoDetail.as_view()),
    path('api/1.0/reviews/', talentos_views.ReviewList.as_view()),
    path('api/1.0/reviews/<review_id>/', talentos_views.ReviewDetail.as_view()),
    path('api/1.0/clients/', usuarios_views.ClientList.as_view()),
    path('api/1.0/clients/<client_id>/', usuarios_views.ClientDetail.as_view()),
    # path('api/', include('rest_framework.urls'), name= 'rest_framework'),
]
