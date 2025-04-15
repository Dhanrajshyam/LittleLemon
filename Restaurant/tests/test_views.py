from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.models import Menu, Booking
from datetime import datetime, timedelta, time, date
from django.utils import timezone  # Import Django's timezone-aware now()
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from Restaurant.serializers import MenuSerializer, BookingSerializer
from django.utils.timezone import make_aware
from django.contrib.auth.models import Group
from Restaurant.models import Restaurant, CustomUser as User
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
        self.user_url = "/user/sign_up/"
        self.user_list_url = reverse('customuser-list')
        self.user_update_url = reverse(
            'customuser-detail', args=[self.user.id])

    def test_create_user(self):
        """Test user creation"""
        data = {"email": "testusercreate@test.com",
                "password": "Testpassword@123",
                "confirm_password": "Testpassword@123"}
        response = self.client.post(self.user_url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_users_unauthenticated(self):
        """Unauthenticated request should not be authorised"""
        self.client.logout()
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



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



class BookingViewSetTestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username='user1@littlelemon.com', password='Passkey@123')
        self.manager = User.objects.create_user(username='managerlittlelemon.com', password='Passkey@123')
        self.branch_manager_group = Group.objects.create(name='Branch_Manager')
        self.manager.groups.add(self.branch_manager_group)

        # Create a restaurant
        self.restaurant = Restaurant.objects.create(
            name = "Little Lemon Restuarant",
            branch = "Chennai",
            address = "#8, 2nd Main Road, Chennai",
            phone = '8346751234',
            email = 'customercarechennai@littlelemon.com',
            opening_time = time(10, 0),
            closing_time = time(22, 0),
            no_of_tables = 5
        )

        # Booking details
        self.booking_date = date.today() + timedelta(days=1)
        self.start_time = time(11, 0)
        self.end_time = time(11, 30)

        self.booking_payload = {
            "branch": "Chennai",
            "name": "John Doe",
            "phone": "1234567890",
            "no_of_guests": 2,
            "booking_date": self.booking_date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "message": "Please reserve near window"
        }

    def authenticate(self, user):
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_booking_success(self):
        self.authenticate(self.user)
        response = self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "Booked")

    def test_prevent_double_booking_same_slot(self):
        self.authenticate(self.user)
        self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        response = self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_branch_manager_can_view_all_bookings(self):
        # Create a booking for a regular user
        self.authenticate(self.user)
        self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        
        self.authenticate(self.manager)
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_normal_user_can_only_see_own_bookings(self):
        other_user = User.objects.create_user(username='user2', password='pass123')
        self.authenticate(other_user)
        self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')

        self.authenticate(self.user)
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(len(response.data), 0)

    def test_cannot_update_past_booking(self):
        past_booking = Booking.objects.create(
            user=self.user,
            branch="Chennai",
            name="John Doe",
            phone="1234567890",
            no_of_guests=2,
            booking_date=date.today() - timedelta(days=1),
            start_time=time(12, 0),
            end_time=time(12, 30),
            status="Booked"
        )
        self.authenticate(self.user)
        url = reverse('booking-detail', kwargs={'pk': past_booking.pk})
        response = self.client.put(url, data=self.booking_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_manager_can_update_status(self):
        self.authenticate(self.user)
        response = self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        booking_id = response.data["id"]

        self.authenticate(self.manager)
        response = self.client.patch(reverse('booking-detail', kwargs={'pk': booking_id}), {"status": "Cancelled"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "Cancelled")

    def test_user_cannot_update_status(self):
        self.authenticate(self.user)
        response = self.client.post(reverse('booking-list'), data=self.booking_payload, format='json')
        booking_id = response.data["id"]

        response = self.client.patch(reverse('booking-detail', kwargs={'pk': booking_id}), {"status": "Cancelled"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_branches(self):
        self.authenticate(self.user)
        response = self.client.get(reverse('booking-branches'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Chennai", response.data["branches"])

    def test_get_working_hours_valid_branch(self):
        self.authenticate(self.user)
        response = self.client.get(reverse('booking-working-hours'), {"branch": "Chennai"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["opening_time"], "10:00")
        self.assertEqual(response.data["closing_time"], "22:00")

    def test_get_working_hours_invalid_branch(self):
        self.authenticate(self.user)
        response = self.client.get(reverse('booking-working-hours'), {"branch": "Invalid"})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

