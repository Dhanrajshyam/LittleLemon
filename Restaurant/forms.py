from enum import unique
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate


class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(username=email, password=password)
            if not self.user:
                raise forms.ValidationError("Invalid credentials")
        return self.cleaned_data

    def get_user(self):
        return self.user
