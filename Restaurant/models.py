from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

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


class CustomUserManager(BaseUserManager):
    """Custom manager for our CustomUser model where email is the username"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom User model that uses email as the primary identifier"""
    
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Make email unique

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # No other fields required

    objects = CustomUserManager()

    def __str__(self):
        return self.email