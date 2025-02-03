from django.test import TestCase
from Restaurant.serializers import MenuSerializer, BookingSerializer
from Restaurant.models import Menu, Booking
from datetime import datetime

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
