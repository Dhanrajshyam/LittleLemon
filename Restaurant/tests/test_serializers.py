from django.test import TestCase
from Restaurant.serializers import MenuSerializer, BookingSerializer
from Restaurant.models import Menu, Booking
from datetime import date, time, timedelta, datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from Restaurant.serializers import UserSerializer
from Restaurant.models import Restaurant

User = get_user_model()

class MenuSerializerTest(TestCase):
    def test_valid_menu_serializer(self):
        """Test serializer with valid data"""
        data = {"title": "Pizza", "price": 9.99, "inventory": 15}
        serializer = MenuSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_menu_serializer(self):
        """Test serializer with missing fields"""
        data = {"title": ""}
        serializer = MenuSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

class BookingSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test@example.com", password="testpass123")
        self.restaurant = Restaurant.objects.create(
            branch="Chennai",
            opening_time=time(10, 0),
            closing_time=time(22, 0)
        )
        self.valid_data = {
            "branch": self.restaurant.branch,
            "name": "John Doe",
            "phone": "9876543210",
            "no_of_guests": 2,
            "booking_date": date.today(),
            "start_time": "10:00",
            "end_time": "22:00",
            "message": "Birthday"
        }

    def get_serializer(self, data):
        class DummyRequest:
            user = self.user
        context = {"request": DummyRequest()}
        return BookingSerializer(data=data, context=context)

    def test_valid_booking(self):
        serializer = self.get_serializer(self.valid_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_invalid_phone_length(self):
        self.valid_data["phone"] = "12345"
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("phone", serializer.errors)

    def test_invalid_guest_count(self):
        self.valid_data["no_of_guests"] = 11
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("no_of_guests", serializer.errors)

    def test_invalid_branch(self):
        self.valid_data["branch"] = "Mumbai"
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("branch", serializer.errors)

    def test_past_booking_date(self):
        self.valid_data["booking_date"] = date.today() - timedelta(days=1)
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("booking_date", serializer.errors)

    def test_start_time_outside_hours(self):
        self.valid_data["start_time"] = time(9, 0)
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("start_time", serializer.errors)

    def test_end_time_outside_hours(self):
        self.valid_data["end_time"] = time(22, 30)
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("end_time", serializer.errors)

    def test_end_time_before_start_time(self):
        self.valid_data["start_time"] = time(14, 0)
        self.valid_data["end_time"] = time(13, 30)
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("end_time", serializer.errors)

    def test_duplicate_booking(self):
        Booking.objects.create(user=self.user, **self.valid_data)
        serializer = self.get_serializer(self.valid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)
        

class UserSerializerTests(TestCase):

    def setUp(self):
        """Set up a user instance and a group for testing."""
        self.user = User.objects.create_user(
            email="testuser@example.com",
            first_name="John",
            last_name="Doe",
            phone_number="1234567890",
            password="Testpass@123"
        )
        self.group = Group.objects.create(name="TestGroup")

    def test_user_serializer_valid_data(self):
        """Test serialization of a user instance"""
        serializer = UserSerializer(instance=self.user, context={"request": None})

        expected_data = {
            "url": serializer.data["url"],  # DRF Hyperlinked field
            "email": "testuser@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "phone_number": "1234567890",
            "groups": []
        }
        self.assertEqual(serializer.data, expected_data)

    def test_user_serializer_valid_input(self):
        """Test deserialization with valid data"""
        valid_data = {
            "email": "newuser@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "0987654321",
            "groups": [self.group.id]
        }
        serializer = UserSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["email"], "newuser@example.com")

    def test_user_serializer_invalid_email(self):
        """Test deserialization with invalid email"""
        invalid_data = {
            "email": "not-an-email",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "0987654321",
            "groups": []
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)  # Email validation should fail

    def test_user_serializer_invalid_phone_number(self):
        """Test deserialization with invalid phone number format"""
        invalid_data = {
            "email": "user@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "123",  # Too short
            "groups": []
        }
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("phone_number", serializer.errors)  # Phone validation should fail

    def test_user_serializer_optional_groups(self):
        """Test serializer behavior when groups are omitted"""
        valid_data = {
            "email": "user@example.com",
            "first_name": "Jane",
            "last_name": "Doe",
            "phone_number": "0987654321"
        }
        serializer = UserSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        self.assertNotIn("groups", serializer.validated_data)  # Groups should be optional
