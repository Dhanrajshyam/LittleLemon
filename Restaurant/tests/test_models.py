from django.test import TestCase
from django.utils import timezone
from Restaurant.models import Menu, Booking, CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

class MenuModelTest(TestCase):
    def setUp(self):
        """Setup a test menu item"""
        self.menu_item = Menu.objects.create(title="Burger", price=5.99, inventory=10)

    def test_menu_str(self):
        """Test the string representation of Menu model"""
        self.assertEqual(str(self.menu_item), "Burger | stock 10")

    def test_menu_price(self):
        """Ensure price is stored correctly"""
        self.assertEqual(self.menu_item.price, 5.99)

class BookingModelTest(TestCase):
    def setUp(self):
        """Setup a test booking"""
        self.booking = Booking.objects.create(name="Alice", no_of_guests=4, booking_date=timezone.now())

    def test_booking_str(self):
        """Test string representation of Booking model"""
        self.assertTrue("Alice" in str(self.booking))

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="Foo@123")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="Foo@123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="Foo@123")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="super@user.com", password="Foo@123", is_superuser=False)
            

class CustomUserTests(TestCase):

    def setUp(self):
        """Set up test data."""
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(
            email="test@example.com", password="TestPass@123", phone_number="9876543210"
        )

    def test_create_user_success(self):
        """Test creating a user with email and password."""
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("TestPass@123"))
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

    def test_create_superuser_success(self):
        """Test creating a superuser."""
        admin_user = self.user_model.objects.create_superuser(
            email="admin@example.com", password="AdminPass@123"
        )
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

    def test_create_user_without_email_fails(self):
        """Test that creating a user without an email raises an error."""
        with self.assertRaises(ValueError):
            self.user_model.objects.create_user(email=None, password="NoEmailPass")

    def test_phone_number_validation(self):
        """Test that phone number must be exactly 10 digits."""
        user = self.user_model.objects.create_user(email="valid@example.com", password="ValidPass@123", phone_number="1234567890")
        self.assertEqual(user.phone_number, "1234567890")

    def test_phone_number_invalid_length(self):
        """Test that an invalid phone number raises a validation error."""
        user = self.user_model(email="wrongphone@example.com", phone_number="123")  # Do not call create_user yet

        with self.assertRaises(ValidationError):
            user.full_clean()  # This triggers model validation before saving
            user.save()