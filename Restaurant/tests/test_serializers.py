from django.test import TestCase
from Restaurant.serializers import MenuSerializer, BookingSerializer
from Restaurant.models import Menu, Booking
from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from Restaurant.serializers import UserSerializer

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

class BookingSerializerTest(TestCase):
    def test_valid_booking_serializer(self):
        """Test serializer with valid data"""
        data = {"name": "John Doe", "no_of_guests": 3, "booking_date": datetime.now().isoformat()}
        serializer = BookingSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_booking_serializer(self):
        """Test serializer with invalid guest number"""
        data = {"name": "John Doe", "no_of_guests": -1, "booking_date": datetime.now().isoformat()}
        serializer = BookingSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        

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
