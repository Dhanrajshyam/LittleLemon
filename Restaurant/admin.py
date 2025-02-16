from django.contrib import admin
from .models import Booking, Menu, CustomUser


# Register your models here.

admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(CustomUser)
