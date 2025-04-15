from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Booking, Menu, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "phone_number", "is_staff", "is_active", 'is_superuser', 'last_login',)
    list_filter = ("email", "phone_number", "is_staff", "is_active", 'is_superuser')
    fieldsets = (
        ('Security', {"fields": ("email", "password")}),
        ('Profile', {'fields': ('first_name', 'last_name', "phone_number")}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", 'first_name', 'last_name', "phone_number", "is_staff", "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email", "phone_number", 'first_name', 'last_name',)
    ordering = ("email",)

# Register your models here.

admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(CustomUser, CustomUserAdmin)
