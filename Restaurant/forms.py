from enum import unique
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate
import re

# Regex pattern for password validation in forms
PASSWORD_REGEX = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,16}$"

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        phone_number = self.cleaned_data.get("phone_number")

        if email and password:
            self.user = authenticate(username=email, password=password)
            if not self.user:
                raise forms.ValidationError("Invalid credentials")
        return self.cleaned_data

    def get_user(self):
        return self.user


class CustomUserSignUpForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'password', 'confirm_password']
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        # Ensure phone number contains exactly 10 digits
        if not re.match(r"^\d{10}$", phone_number):
            raise forms.ValidationError("Phone number must be exactly 10 digits.")

        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check password regex
        if not re.match(PASSWORD_REGEX, password):
            raise forms.ValidationError("Password must be 8-16 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%^&*).")

        # Check if passwords match
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data