from django.test import TestCase
from Restaurant.forms import CustomUserSignUpForm, LoginForm
from Restaurant.models import CustomUser

class CustomUserSignUpFormTests(TestCase):

    def test_valid_data(self):
        """Test form with valid data"""
        form = CustomUserSignUpForm(data={
            "email": "user@example.com",
            "phone_number": "1234567890",
            "password": "Secure@123",
            "confirm_password": "Secure@123"
        })
        self.assertTrue(form.is_valid())

    def test_invalid_phone_number(self):
        """Test form with invalid phone number (not 10 digits)"""
        form = CustomUserSignUpForm(data={
            "email": "user@example.com",
            "phone_number": "123",
            "password": "Secure@123",
            "confirm_password": "Secure@123"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("phone_number", form.errors)

    def test_password_not_matching(self):
        """Test form when passwords do not match"""
        form = CustomUserSignUpForm(data={
            "email": "user@example.com",
            "phone_number": "1234567890",
            "password": "Secure@123",
            "confirm_password": "Wrong@123"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)  # Django stores general form errors under '__all__'

    def test_password_does_not_meet_criteria(self):
        """Test form with weak password (missing special character)"""
        form = CustomUserSignUpForm(data={
            "email": "user@example.com",
            "phone_number": "1234567890",
            "password": "WeakPass1",
            "confirm_password": "WeakPass1"
        })
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)


class LoginFormTests(TestCase):

    def test_valid_login_form(self):
        """Test login form with valid data"""
        form = LoginForm(data={"email": "user@example.com", "password": "Secure@123"})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        """Test login form with invalid email format"""
        form = LoginForm(data={"email": "invalid-email", "password": "Secure@123"})
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_missing_password(self):
        """Test login form with missing password"""
        form = LoginForm(data={"email": "user@example.com"})
        self.assertFalse(form.is_valid())
        self.assertIn("password", form.errors)
