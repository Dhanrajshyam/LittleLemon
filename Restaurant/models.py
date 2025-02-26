from typing import Required
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission


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
    
    def _create_user(self, email, password=None, **extra_fields):
        """Create and return a user"""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        
        # Assign permissions only for regular users
        if not user.is_superuser:
            user.user_permissions.clear()  # Remove all permissions first
            
            # Get specific permissions to assign
            allowed_permissions = [
                "add_order", "change_order", "view_order",  # Example: Order model permissions
                "view_menuitem",  # Example: View-only permission for MenuItem
            ]
            content_types = ContentType.objects.all()  # Get all content types
            for ct in content_types:
                for perm in Permission.objects.filter(content_type=ct, codename__in=allowed_permissions):
                    user.user_permissions.add(perm)

        return user
    
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user"""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)

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