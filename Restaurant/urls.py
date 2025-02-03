from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

userrouter = DefaultRouter(trailing_slash=False)
userrouter.register(r"users", UserViewSet, basename='user')

urlpatterns = [
    path("",views.index, name="home"),
    path("",include(userrouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]