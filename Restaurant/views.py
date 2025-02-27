from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Menu, Booking, CustomUser
from .forms import CustomUserSignUpForm, LoginForm
from django.shortcuts import render, redirect
from .utils import generate_email_verification_token, verify_email_token, send_mailgun_email, send_verification_email
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    """Homepage of the application"""
    return render(request, 'index.html', {})


def terms_n_conditions(request):
    """Terms and conditions page"""
    return render(request, 'terms_n_conditions.html', {})


# def verify_email(request, uidb64, token):
#     if verify_email_token(uidb64, token):
#         return HttpResponse("email verified successfully! you can now log in.")
#     return HttpResponse("invalid verification link or expired.")

def user_login(request):
    """Login the user"""
    if request.method == "POST":
        form = LoginForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                form.add_error('password', "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    """Logout the user"""
    logout(request)
    return redirect("home")


class UserSignUpView(CreateView):
    """Sign up a new user"""
    model = CustomUser
    form_class = CustomUserSignUpForm
    template_name = "user_sign_up.html"

    def post(self, request):
        form = CustomUserSignUpForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            user = form.save(commit=False)
            # Set hashed password - Hasher Argon2
            user.set_password(form.cleaned_data["password"])
            user.is_active = True  # Late make it false to set users Inactive until email verification
            user.save()
            return render(request, "sign_up_success.html")
        return render(request, "user_sign_up.html", {"form": form})


class UserViewSet(viewsets.ModelViewSet):
    """
    Handles user-related operations.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """Create a new user"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created Successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """Update a user"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a user"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a user"""
        return super().destroy(request, *args, **kwargs)
    

class MenuViewSet(viewsets.ModelViewSet):
    """
    Handles menu-related operations.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def list(self, request, *args, **kwargs):
        """Retrieve a list of menu items"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new menu"""
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a menu item by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a menu item by ID"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a menu item by ID"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a menu by ID"""
        return super().destroy(request, *args, **kwargs)


class BookingViewSet(viewsets.ModelViewSet):
    """
    Handles booking-related operations.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        """Retrieve a list of bookings"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new booking"""
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a booking by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a booking by ID"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a booking by ID"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a booking by ID"""
        return super().destroy(request, *args, **kwargs)
