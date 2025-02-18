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
    path('user/sign_up/', views.UserSignUpView.as_view(), name = "user_sign_up" ),
    path('terms/', views.terms_n_conditions, name= "terms_n_conditions"),
    # path("verify-email/<uidb64>/<token>/", views.verify_email, name="verify_email"),
]