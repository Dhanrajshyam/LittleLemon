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
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = User.objects.all()
        users = UserSerializer(queryset, many=True, context = {'request': request})
        return Response(users.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(object, context = {'request': request})
        return Response(user.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user = UserSerializer(data = request.data, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({'message': 'User created Successfully!'}, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(instance = object, data = request.data, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({"message": "User updated Successfully"}, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        object = get_object_or_404(User, pk=pk)
        user = UserSerializer(instance= object, data= request.data, partial=True, context = {'request': request})
        if user.is_valid():
            user.save()
            return Response({"message": "User updated Successfully!"}, status=status.HTTP_200_OK)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk=None):
        object = get_object_or_404(User, pk=pk)
        object.delete()
        return Response({"message": "User deleted Successfully!"}, status=status.HTTP_200_OK)
    
    
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[permissions.IsAuthenticated]
