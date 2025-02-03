from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu, Booking
from datetime import datetime
from django.utils import timezone  # Import Django's timezone-aware now()

class UserViewSetTest(TestCase):
    def setUp(self):
        """Set up users for testing"""
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.admin_user = User.objects.create_superuser(username="administrator", password="adminpassword")

        self.client.login(username="testuser", password="testpassword")
        self.user_url = "/api/users"

    def test_list_users_authenticated(self):
        """Authenticated user should be able to list users"""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_users_unauthenticated(self):
        """Unauthenticated request should not be authorised"""
        self.client.logout()
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class MenuViewSetTest(TestCase):
    def setUp(self):
        """Set up menu items"""
        self.client = APIClient()
        self.menu_item = Menu.objects.create(title="Pizza", price=10.99, inventory=20)
        self.menu_url = "/api/menu"

    def test_list_menu_items(self):
        """Ensure menu items are listed correctly"""
        response = self.client.get(self.menu_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_item(self):
        """Create a new menu item"""
        data = {"title": "Burger", "price": 5.99, "inventory": 10}
        response = self.client.post(self.menu_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookingViewSetTest(TestCase):
    def setUp(self):
        """Set up booking entries"""
        self.client = APIClient()
        self.booking = Booking.objects.create(name="John Doe", no_of_guests=2, booking_date=timezone.now())

        # Authenticate User
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        self.booking_url = "/api/booking"

    def test_list_bookings(self):
        """Test booking listing"""
        response = self.client.get(self.booking_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_booking(self):
        """Test booking creation"""
        data = {"name": "Alice", "no_of_guests": 3, "booking_date": timezone.now()}
        response = self.client.post(self.booking_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
