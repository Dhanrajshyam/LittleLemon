from rest_framework import serializers
from .models import Menu, Booking, CustomUser
from django.contrib.auth.models import Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(required = False, many=True, queryset=Group.objects.all())
    class Meta:
        model = CustomUser
        fields = ["url", "email", "first_name", "last_name", "phone_number", "groups"]
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'