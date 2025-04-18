# From Django Library
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

# From Django Rest Framework
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes
from rest_framework import filters

# From Python Library
from datetime import datetime

# From the application - Resturant
from .serializers import UserSerializer, MenuSerializer, BookingSerializer, RestuarantSerializer, HolidaySerializer
from .models import Menu, Booking, CustomUser, Restaurant, Holiday
from .forms import CustomUserSignUpForm, LoginForm
from .utils import generate_email_verification_token, verify_email_token, send_mailgun_email, send_verification_email
from .utils import is_slot_available
from .permissions import IsBranchManagerOrReadOnly, IsBranchManager


# Create your views here.

def health_check(request):
    return JsonResponse({"status": "ok"})

def index(request):
    """Homepage of the application"""
    return render(request, 'index.html', {})


def about(request):
    """About page"""
    return render(request, 'about.html', {})


def menu(request):
    """Menu page"""
    # Fetch all menu items directly from the database
    menu_list = Menu.objects.all()

    # Prepare context for the template
    context = {
        'menu_list': menu_list
    }
    return render(request, 'menu.html', context)

@login_required
def book(request):
    """Book a Reservation in the restaurant"""
    return render(request, 'book.html', {})

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
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["email", "first_name", "last_name", "phone_number"]
    ordering_fields = ["first_name", "last_name", "groups__name"]

    def get_queryset(self):
        """
        Restrict data based on user groups
        - Users with Branch_Manager group can perform all CRUD operations on all users.
        - Normal users can view their own profile/account details and perform update/delete(account deletion) on it. 
        """
        user = self.request.user
        if user.groups.filter(name='Branch_Manager').exists():
            return get_user_model().objects.all()  # Branch Managers get all users
        # Normal users get only their own data
        return get_user_model().objects.filter(id=user.id)

    def create(self, request, *args, **kwargs):
        """Create a new user"""
        if request.method == 'POST' and not request.user.groups.filter(name="Branch_Manager").exists():
            return Response({'error': f'Normal user can create an account from UI - Sign up page.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created Successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """Retrieve a list of users"""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a user"""
        return super().retrieve(request, *args, **kwargs)

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
    permission_classes = [IsBranchManagerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'category']
    ordering_fields = ['title', 'description', 'category', 'price', 'inventory']

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
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user__email", "name", "phone"]
    ordering_fields = ["name",  "booking_date", "status"]

    def get_queryset(self):
        """
        Restrict data based on user groups.
        - Users with Branch_Manager group can perform all CRUD operations on all booking by all users.
        - Normal users(Authenticated) can view the list of bookings booked by them and its booking details.
        - Anonymous (Unauthenticated) Users can't access the booking API endpoints.
        """
        user = self.request.user
        if user.groups.filter(name='Branch_Manager').exists():
            return Booking.objects.all()  # Branch Managers get all user's bookings
        # Normal users see only their own bookings
        return Booking.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        """Retrieve a list of bookings"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new booking"""
        data=request.data
        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception=True)
        
        # Book if requested date and time is available
        try:
            serializer.save(user=self.request.user, status=Booking.Status.PENDING)
            slot_available = is_slot_available(
                serializer.validated_data["branch"],
                serializer.validated_data["booking_date"],
                serializer.validated_data["start_time"],
                serializer.validated_data["end_time"]
            )
            if slot_available:
                serializer.save(status=Booking.Status.BOOKED)
            else:
                serializer.save(status=Booking.Status.FAILED)
                return Response({"error": "One or more slots are already booked. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            serializer.save(status=Booking.Status.FAILED)
            return Response({"error": "One or more slots are already booked. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a booking by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a booking by ID"""

        instance = self.get_object()
        user = request.user

        # Prevent updates on past bookings
        if instance.booking_date < now().date():
            return Response({"error": "Cannot modify past bookings"}, status=400)

        # Restrict normal users from updating status
        if "status" in request.data and not user.groups.filter(name='Branch_Manager').exists():
            return Response({"error": "Only Branch Managers can change booking status"}, status=403)

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a booking by ID"""

        instance = self.get_object()
        user = request.user

        # Prevent updates on past bookings
        if instance.booking_date < now().date():
            return Response({"error": "Cannot modify past bookings"}, status=400)

        # Restrict normal users from updating status
        if "status" in request.data and not user.groups.filter(name='Branch_Manager').exists():
            return Response({"error": "Only Branch Managers can change booking status"}, status=403)

        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a booking by ID"""

        instance = self.get_object()

        # Prevent deletes on past bookings
        if instance.booking_date < now().date():
            return Response({"error": "Cannot delete past bookings"}, status=400)

        return super().destroy(request, *args, **kwargs)
        
    @action(detail=False, methods=["get"])
    def branches(self, request):
        """
        Returns a list of restaurant branches.
        """
        branches = Restaurant.objects.values_list("branch", flat=True)
        return Response({"branches": list(branches)})
    
    @action(detail=False, methods=["get"])
    def working_hours(self, request):
        """
        Returns the working hours of a specific branch.
        """
        branch = request.query_params.get("branch")
        if not branch:
            return Response({"error": "Branch parameter is required. e.g. /api/booking/working_hours?branch=Vellore"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            restaurant = Restaurant.objects.get(branch=branch)
            opening_time = restaurant.opening_time.strftime("%H:%M")
            closing_time = restaurant.closing_time.strftime("%H:%M")
            return Response({"opening_time": opening_time, "closing_time": closing_time})
        except Restaurant.DoesNotExist:
            return Response({"error": "Branch not found."}, status=status.HTTP_404_NOT_FOUND)


class RestaurantViewset(viewsets.ModelViewSet):
    """
    Handles restaurant-related operations.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestuarantSerializer
    permission_classes = [IsBranchManager]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['branch', 'phone']
    ordering_fields = ['branch']

    def list(self, request, *args, **kwargs):
        """Retrieve a list of restaurants"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new restaurant-branch"""
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a restaurant by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a restaurant by ID"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a restaurant by ID"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a restaurant by ID"""
        return super().destroy(request, *args, **kwargs)
    
class HolidayViewSet(viewsets.ModelViewSet):
    """
    Handles holiday-related operations.
    """
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsBranchManager]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['holiday_date', 'description']
    ordering_fields = ['holiday_date', 'description']

    def list(self, request, *args, **kwargs):
        """Retrieve a list of holidays"""
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Create a new holiday"""
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Retrieve a holiday by ID"""
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """Update a holiday by ID"""
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """Partially update a holiday by ID"""
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Delete a holiday by ID"""
        return super().destroy(request, *args, **kwargs)
