from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MenuViewSet, BookingViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename='user')
router.register(r"menu", MenuViewSet)
router.register(r"booking", BookingViewSet)

urlpatterns = [
    path("",views.index, name="home"),
    path("api/",include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]