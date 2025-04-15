from django import forms
from .models import CustomUser
import re
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Regex pattern for password validation in forms
PASSWORD_REGEX = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,16}$"


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class CustomUserSignUpForm(forms.ModelForm):
    email = forms.EmailField()
    phone_number = forms.CharField(required=False, max_length=10)
    password = forms.CharField(required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'phone_number', 'password', 'confirm_password']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        # Ensure phone number contains exactly 10 digits
        if phone_number and not re.match(r"^\d{10}$", phone_number):
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits.")

        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check password regex
        if not re.match(PASSWORD_REGEX, password):
            raise forms.ValidationError(
                "Password must be 8-16 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character (!@#$%^&*).")

        # Check if passwords match
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
