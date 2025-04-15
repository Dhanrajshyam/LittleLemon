from django.test import TestCase
from django.utils import timezone
from Restaurant.models import Menu, Booking, CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import date, time, timedelta
from django.db import IntegrityError

class MenuModelTest(TestCase):
    def setUp(self):
        self.valid_data = {
            "title": "Masala Dosa",
            "description": "Crispy dosa with spiced potato filling",
            "category": "South Indian",
            "price": 65.50,
            "inventory": 15,
            "image_filename": "/static/img/menu/dosa.png"
        }

    def test_create_menu_item_successfully(self):
        menu_item = Menu.objects.create(**self.valid_data)
        self.assertEqual(menu_item.title, "Masala Dosa")
        self.assertEqual(menu_item.description, "Crispy dosa with spiced potato filling")
        self.assertEqual(menu_item.category, "South Indian")
        self.assertEqual(menu_item.price, 65.50)
        self.assertEqual(menu_item.inventory, 15)
        self.assertEqual(menu_item.image_filename, "/static/img/menu/dosa.png")
        self.assertEqual(str(menu_item), f"Masala Dosa | stock 15")

    def test_default_values(self):
        menu_item = Menu.objects.create(
            title="Boiled Egg"
        )
        self.assertEqual(menu_item.description, "")
        self.assertEqual(menu_item.category, "None")
        self.assertEqual(menu_item.price, 0.00)
        self.assertEqual(menu_item.inventory, 0)
        self.assertEqual(menu_item.image_filename, "/static/img/menu/boil.png")

    def test_string_representation(self):
        menu_item = Menu.objects.create(**self.valid_data)
        self.assertEqual(str(menu_item), f"{menu_item.title} | stock {menu_item.inventory}")

    def test_unique_title_constraint(self):
        Menu.objects.create(**self.valid_data)
        with self.assertRaises(IntegrityError):
            Menu.objects.create(**self.valid_data)  # duplicate title

class BookingModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(email="user@example.com", password="pass123")
        self.default_data = {
            "user": self.user,
            "branch": "Vellore",
            "name": "John Doe",
            "phone": "9876543210",
            "no_of_guests": 3,
            "booking_date": date.today() + timedelta(days=1),
            "start_time": time(18, 0),
            "end_time": time(18, 30),
            "message": "Window seat preferred"
        }

    def test_create_booking_with_defaults(self):
        booking = Booking.objects.create(**self.default_data)
        self.assertEqual(booking.status, Booking.Status.PENDING)
        self.assertEqual(booking.branch, "Vellore")
        self.assertEqual(booking.phone, "9876543210")
        self.assertEqual(str(booking), f"{booking.name} | {booking.booking_date} | User: {booking.user.email}")

    def test_booking_status_choices(self):
        booking = Booking.objects.create(**self.default_data)
        booking.status = Booking.Status.BOOKED
        booking.save()
        self.assertEqual(booking.status, "BOOKED")

    def test_invalid_phone_number_should_raise_validation_error(self):
        self.default_data["phone"] = "12345"  # Invalid phone number
        booking = Booking(**self.default_data)
        with self.assertRaises(ValidationError) as context:
            booking.full_clean()
        self.assertIn("Phone number must be exactly 10 digits", str(context.exception))

    def test_created_at_is_auto_populated(self):
        booking = Booking.objects.create(**self.default_data)
        self.assertIsNotNone(booking.created_at)
        self.assertLessEqual(booking.created_at, timezone.now())

    def test_booking_str_representation(self):
        booking = Booking.objects.create(**self.default_data)
        expected_str = f"{booking.name} | {booking.booking_date} | User: {booking.user.email}"
        self.assertEqual(str(booking), expected_str)

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="Foossas@123")
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
            User.objects.create_user(email="", password="Foossas@123")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="Foossas@123")
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
                email="super@user.com", password="Foossas@123", is_superuser=False)
            

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