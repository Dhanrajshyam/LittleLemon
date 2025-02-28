from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu, Booking
from datetime import datetime
from django.utils import timezone  # Import Django's timezone-aware now()
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Restaurant.serializers import MenuSerializer, BookingSerializer
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class UserViewSetTest(TestCase):
    def setUp(self):
        """Set up users for testing"""
        User = get_user_model()
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="testuser@test.com", password="Testpassword@123")
        self.admin_user = User.objects.create_superuser(
            email="administrator@test.com", password="Adminpassword@123")

        # Grant permissions to test user to view users
        permission = Permission.objects.get(codename='view_customuser')
        self.user.user_permissions.add(permission)

        # Force authenticate as Django Axes (a security middleware) is interfering with authentication.
        self.client.force_authenticate(user=self.user)
        # self.client.login(email="testuser@test.com", password="Testpassword@123")
        self.user_url = "/api/users"
        self.user_list_url = reverse('customuser-list')
        self.user_update_url = reverse(
            'customuser-detail', args=[self.user.id])

    def test_create_user(self):
        """Test user creation"""
        data = {"email": "testusercreate@test.com",
                "password": "Testpassword@123"}
        response = self.client.post(self.user_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("message"),
                         "User created Successfully!")

    def test_list_users(self):
        """Test listing users"""
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_user(self):
        """Test updating a user"""
        data = {'email': self.user.email, 'first_name': 'Test_Name'}
        response = self.client.put(self.user_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test_Name')

    def test_partial_update_user(self):
        """Test partially updating a user"""
        data = {'first_name': 'New_Test_Name', 'last_name': 'Test_Last_Name'}
        response = self.client.patch(self.user_update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'New_Test_Name')
        self.assertEqual(self.user.last_name, 'Test_Last_Name')

    def test_delete_user(self):
        """Test deleting a user"""
        response = self.client.delete(self.user_update_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(get_user_model().objects.filter(
            id=self.user.id).exists())

    def test_unauthenticated_user_access(self):
        """Ensure unauthenticated users cannot access user endpoints"""
        self.client.logout()
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_users_unauthenticated(self):
        """Unauthenticated request should not be authorised"""
        self.client.logout()
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



class MenuViewSetTests(APITestCase):

    def setUp(self):
        """Set up test data."""
        self.menu1 = Menu.objects.create(title="Pasta", price=10.99, inventory=5)
        self.menu2 = Menu.objects.create(title="Pizza", price=12.99, inventory=8)

        self.valid_data = {
            "title": "Burger",
            "price": 8.99,
            "inventory": 10,
        }

        self.invalid_data = {
            "title": "",
            "price": "invalid_price",  # Invalid price format
            "inventory": -5,  # Negative inventory is invalid
        }

        self.url_list = reverse("menu-list")  # URL for listing and creating menu items
        self.url_detail = lambda menu_id: reverse("menu-detail", kwargs={"pk": menu_id})  # URL for specific menu item

    def test_list_menus(self):
        """Test retrieving a list of menu items."""
        response = self.client.get(self.url_list)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu(self):
        """Test creating a new menu item."""
        response = self.client.post(self.url_list, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)  # Two from setUp, one new

    def test_create_menu_invalid_data(self):
        """Test creating a menu item with invalid data."""
        response = self.client.post(self.url_list, self.invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_menu(self):
        """Test retrieving a specific menu item by ID."""
        response = self.client.get(self.url_detail(self.menu1.id))
        serializer = MenuSerializer(self.menu1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_menu(self):
        """Test updating a menu item."""
        updated_data = {
            "title": "Pasta Alfredo",
            "price": 11.99,
            "inventory": 6,
        }
        response = self.client.put(self.url_detail(self.menu1.id), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu1.refresh_from_db()
        self.assertEqual(self.menu1.title, "Pasta Alfredo")

    def test_partial_update_menu(self):
        """Test partially updating a menu item."""
        partial_data = {"price": 13.99}  # Only updating price
        response = self.client.patch(self.url_detail(self.menu1.id), partial_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu1.refresh_from_db()
        self.assertEqual(float(self.menu1.price), 13.99)

    def test_delete_menu(self):
        """Test deleting a menu item."""
        response = self.client.delete(self.url_detail(self.menu1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Menu.objects.filter(id=self.menu1.id).exists())



class BookingViewSetTests(APITestCase):

    def setUp(self):
        """Set up test data and authentication."""
        self.user = get_user_model().objects.create_user(email="testuser@example.com", password="testpassword")
        self.client.force_authenticate(user=self.user)  # Authenticate the client

        self.booking1 = Booking.objects.create(
            name="John Doe",
            no_of_guests=4,
            booking_date=make_aware(datetime.now() + timedelta(days=1))  # Future booking
        )

        self.booking2 = Booking.objects.create(
            name="Jane Doe",
            no_of_guests=2,
            booking_date=make_aware(datetime.now() + timedelta(days=2))
        )

        self.valid_data = {
            "name": "Alice Smith",
            "no_of_guests": 3,
            "booking_date": (datetime.now() + timedelta(days=3)).isoformat()
        }

        self.invalid_data = {
            "name": "",
            "no_of_guests": -1,  # Invalid guest count
            "booking_date": "invalid-date-format"
        }

        self.url_list = reverse("booking-list")  # URL for listing and creating bookings
        self.url_detail = lambda booking_id: reverse("booking-detail", kwargs={"pk": booking_id})  # URL for specific booking

    def test_list_bookings(self):
        """Test retrieving a list of bookings."""
        response = self.client.get(self.url_list)
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_booking(self):
        """Test creating a new booking."""
        response = self.client.post(self.url_list, self.valid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 3)  # Two from setUp, one new

    def test_create_booking_invalid_data(self):
        """Test creating a booking with invalid data."""
        response = self.client.post(self.url_list, self.invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_booking(self):
        """Test retrieving a specific booking by ID."""
        response = self.client.get(self.url_detail(self.booking1.id))
        serializer = BookingSerializer(self.booking1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_booking(self):
        """Test updating a booking."""
        updated_data = {
            "name": "Updated Name",
            "no_of_guests": 5,
            "booking_date": (datetime.now() + timedelta(days=4)).isoformat()
        }
        response = self.client.put(self.url_detail(self.booking1.id), updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking1.refresh_from_db()
        self.assertEqual(self.booking1.name, "Updated Name")

    def test_partial_update_booking(self):
        """Test partially updating a booking."""
        partial_data = {"no_of_guests": 6}
        response = self.client.patch(self.url_detail(self.booking1.id), partial_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.booking1.refresh_from_db()
        self.assertEqual(self.booking1.no_of_guests, 6)

    def test_delete_booking(self):
        """Test deleting a booking."""
        response = self.client.delete(self.url_detail(self.booking1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Booking.objects.filter(id=self.booking1.id).exists())

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot access booking endpoints."""
        self.client.force_authenticate(user=None)  # Remove authentication
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


