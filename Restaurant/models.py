from typing import Required
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib import auth
from .managers import CustomUserManager
# from django.contrib.auth.hashers import make_password


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(default=0)
    booking_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.name} | {self.booking_date.date()}'

class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    inventory =models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.title} | stock {self.inventory}'    

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