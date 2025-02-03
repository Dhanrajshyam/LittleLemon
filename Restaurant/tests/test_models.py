from django.test import TestCase
from django.utils import timezone
from Restaurant.models import Menu, Booking

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
