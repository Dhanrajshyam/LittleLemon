from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, MenuViewSet, BookingViewSet, index, about, menu , user_login, user_logout, UserSignUpView, terms_n_conditions

router = DefaultRouter(trailing_slash=False)
router.register(r"users", UserViewSet, basename="customuser")
router.register(r"menu", MenuViewSet)
router.register(r"booking", BookingViewSet)

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("menu/", menu, name="menu"),
    path("api/", include(router.urls)),
    path('user/sign_up/', UserSignUpView.as_view(), name = "user_sign_up" ),
    path('terms/', terms_n_conditions, name= "terms_n_conditions"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),


    # path("verify-email/<uidb64>/<token>/", views.verify_email, name="verify_email"),
]