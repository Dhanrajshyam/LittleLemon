from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Menu, Booking

# Create your views here.
def index(request):
    """Homepage of the application"""
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ViewSet):
    """
    Handles user-related operations.
    """
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        """Retrieve a list of users"""
        queryset = User.objects.all()
        users = UserSerializer(queryset, many=True, context = {'request': request})
        return Response(users.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        """Retrieve a user by ID"""
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(object, context = {'request': request})
        return Response(user.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Create a new user"""
        user = UserSerializer(data = request.data, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({'message': 'User created Successfully!'}, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        """Update a user by ID"""
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(instance = object, data = request.data, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({"message": "User updated Successfully"}, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        """Partially update a user by ID"""
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(instance= object, data= request.data, partial=True, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({"message": "User updated Successfully!"}, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        """Delete a user by ID"""
        object = get_object_or_404(User, pk=pk)
        object.delete()
        return Response({"message": "User deleted Successfully!"}, status=status.HTTP_200_OK)
    
    
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
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]

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
