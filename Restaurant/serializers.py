from rest_framework import serializers
from .models import Menu, Booking, CustomUser, BookedSlot
from django.contrib.auth.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(required = False, many=True, queryset=Group.objects.all())
    class Meta:
        model = CustomUser
        fields = ["url", "email", "first_name", "last_name", "phone_number", "groups"]
        
class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['url', 'id', 'title', 'description', 'category', 'price', 'inventory', 'image_filename']
        
class BookedSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSlot
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    slots = BookedSlotSerializer(many=True, write_only=True)
    booked_slots = BookedSlotSerializer(many=True, read_only=True)
    phone = serializers.CharField(max_length=10, min_length=10)
    no_of_guests = serializers.IntegerField(min_value=1, max_value=10, default=1)
    
    class Meta:
        model = Booking
        fields = ["id", "user", "name", "phone", "no_of_guests", "booking_date", "message", "status", "slots", "booked_slots"]
        read_only_fields = ["user", "status", "booked_slots"]
    
    def validate_slots(self, slots):
        """Check if slots exceeds the limit. Maximum 3 slots allowed"""
        if len(slots) > 3:
            raise serializers.ValidationError("Maximum 3 slots allowed per booking.")
        return slots
    
    def validate_phone(self, phone):
        """Ensure phone number contains exactly 10 digits"""
        if not phone.isdigit() or len(phone) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return phone

