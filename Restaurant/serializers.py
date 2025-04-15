from rest_framework import serializers
from .models import Menu, Booking, CustomUser, Restaurant, Holiday
from django.contrib.auth.models import Group
from datetime import date, timedelta, time, datetime


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(required = False, many=True, queryset=Group.objects.all())
    class Meta:
        model = CustomUser
        fields = ["url", "email", "first_name", "last_name", "phone_number", "groups"]
        
class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['url', 'id', 'title', 'description', 'category', 'price', 'inventory', 'image_filename']        

class RestuarantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['url', 'id', 'name', 'branch', 'address', 'phone', 'email', 'opening_time', 'closing_time', 'no_of_tables']
        read_only_fields = ['name']
        
class BookingSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=10, min_length=10)
    no_of_guests = serializers.IntegerField(min_value=1, max_value=10, default=1)
    branch = serializers.ChoiceField(choices=[], required=True)
    booking_date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()
    message = serializers.CharField(max_length=255, required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Restaurant  # Import here to avoid circular import
        self.fields['branch'].choices = list(
            Restaurant.objects.values_list('branch', flat=True)
        )
    
    class Meta:
        model = Booking
        fields = ["id", "user", "branch", "name", "phone", "no_of_guests", "booking_date", "start_time", "end_time", "message", "status"]
        read_only_fields = ["user", "status"]
        
    def validate(self, attrs):
        user = self.context["request"].user
        booking_date = attrs["booking_date"]
        start_time = attrs["start_time"]
        end_time = attrs["end_time"]

        if Booking.objects.filter(
            user=user,
            booking_date=booking_date,
            start_time=start_time,
            end_time=end_time,
        ).exists():
            raise serializers.ValidationError("You already have a booking that overlaps with this time slot.")

        return attrs
    
    def validate_phone(self, phone):
        """Ensure phone number contains exactly 10 digits"""
        if not phone.isdigit() or len(phone) != 10:
            raise serializers.ValidationError("Phone number must be exactly 10 digits.")
        return phone
    
    def validate_branch(self, branch):
        """Ensure branch exists"""
        if not Restaurant.objects.filter(branch=branch).exists():
            raise serializers.ValidationError("Invalid branch. View available branches on /api/booking/branches")
        return branch
    
    def validate_booking_date(self, booking_date):
        """Ensure booking date is either today or future date"""
        if not isinstance(booking_date, date):
            raise serializers.ValidationError("Booking date must be a valid date. Format: YYYY-MM-DD")
        if booking_date < date.today():
            raise serializers.ValidationError("Booking date must be today or future date.")
        return booking_date
    
    def validate_start_time(self, start_time):
        """Ensure start time is within restaurant opening hours and closing hours"""
        if not isinstance(start_time, time):
            raise serializers.ValidationError("Start time must be a valid time. Format: HH:MM")
        restaurant = Restaurant.objects.get(branch=self.initial_data["branch"])
        closing_datetime = datetime.combine(datetime.today().date(), restaurant.closing_time)
        adjusted_closing_datetime = closing_datetime - timedelta(minutes=30)
        closing_time = adjusted_closing_datetime.time()
        if start_time < restaurant.opening_time or start_time > closing_time:
            raise serializers.ValidationError(f"Start time must be within restaurant working hours. {restaurant.opening_time} - {closing_time}")
        return start_time
    
    def validate_end_time(self, end_time):
        """Ensure end time is within restaurant opening hours and closing hours"""
        if not isinstance(end_time, time):
            raise serializers.ValidationError("End time must be a valid time. Format: HH:MM")
        restaurant = Restaurant.objects.get(branch=self.initial_data["branch"])
        if end_time <= time.fromisoformat(self.initial_data.get("start_time")):
            raise serializers.ValidationError("End time must be greater than start time.")
        if end_time < restaurant.opening_time or end_time > restaurant.closing_time:
            raise serializers.ValidationError(f"End time must be within restaurant working hours. {restaurant.opening_time} - {restaurant.closing_time}")
        return end_time

class HolidaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Holiday
        fields = ['url', 'id', 'holiday_date', 'description']
        
