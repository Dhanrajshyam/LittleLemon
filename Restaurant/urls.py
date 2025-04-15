from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MenuViewSet, BookingViewSet, index, about, menu, book, user_login, user_logout, UserSignUpView, terms_n_conditions
from .views import RestaurantViewset, HolidayViewSet, health_check
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Little Lemon API",
        default_version='v1',
        description="API documentation for Little Lemon",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Routers
router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename="customuser")
router.register(r"menu", MenuViewSet)
router.register(r"booking", BookingViewSet)
router.register(r"restaurant", RestaurantViewset)
router.register(r"holiday", HolidayViewSet)

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("menu/", menu, name="menu"),
    path("book/", book, name="book"),
    path('user/sign_up/', UserSignUpView.as_view(), name = "user_sign_up" ),
    path('terms/', terms_n_conditions, name= "terms_n_conditions"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),\
    #API
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #Documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #Health Check
    path("health/", health_check),
    # path("verify-email/<uidb64>/<token>/", views.verify_email, name="verify_email"),
]


