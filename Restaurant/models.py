from typing import Required
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib import auth
from .managers import CustomUserManager
from django.core.exceptions import ValidationError
from datetime import time, timedelta, datetime
# from django.contrib.auth.hashers import make_password


# Create your models here.

class CustomUser(AbstractUser):
    """Custom User model that uses email as the primary identifier"""
    
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Make email unique
    phone_number = models.CharField(
        max_length=10,
        null=True, blank=True,
        validators=[RegexValidator(r"^\d{10}$", message="Phone number must be exactly 10 digits.")]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # No other fields required

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Holiday(models.Model):
    """Holiday model"""
    holiday_date = models.DateField()
    description = models.CharField(blank=True, max_length=255)
    
    def __str__(self):
        return f'{self.holiday_date} | {self.description}'
    
class Timeslot(models.Model):
    """Reference Timeslots model"""
    slot_name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self):
        return f"{self.slot_name} | {self.start_time} to {self.end_time}"
    
class BookedSlot(models.Model):
    """Booked slots model"""
    booking = models.ForeignKey("Booking", on_delete=models.CASCADE, related_name="booked_slots")
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time} - {self.end_time}"

class Booking(models.Model):
    """Booking model"""
    
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"  # Default status after booking request
        BOOKED = "BOOKED", "Booked"  # Successfully confirmed
        FAILED = "FAILED", "Failed"  # Payment or system failure or booked by other user
        CANCELED = "CANCELED", "Canceled"  # User requested cancellation
        COMPLETED = "COMPLETED", "Completed"  # Successfully served

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r"^\d{10}$", message="Phone number must be exactly 10 digits.")]
    )
    no_of_guests = models.PositiveIntegerField(default=0)
    booking_date = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        """Ensure time slot is available before booking"""
        booked_slots = BookedSlot.objects.filter(
            booking__booking_date__date=self.booking_date.date(),
            start_time=self.booking_date.time(),
        )
        if booked_slots.exists():
            raise ValidationError("Selected time slot is already booked. Choose another slot.")

    def __str__(self):
        return f'{self.name} | {self.booking_date.date()} | User: {self.user.email}'

class Menu(models.Model):
    """Menu model"""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=255, default="None", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory =models.PositiveIntegerField(default=0)
    image_filename = models.CharField(max_length=255, default="/static/img/menu/boil.png")
    
    def __str__(self):
        return f'{self.title} | stock {self.inventory}'    

