# 🛠 Django Test Results

![Django Tests](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml/badge.svg)

This file documents all the test cases executed in the Django project and their latest execution status in GitHub Actions.

---

## ✅ **How to Run Tests Locally**
Run the following command in your terminal to execute tests:
```bash
python manage.py test --keepdb

📝 Test Case Summary
Models
Test Case	Description	Status
test_menu_str	Ensures that the __str__ method of the Menu model returns the correct string representation	✅
test_booking_str	Ensures that the __str__ method of the Booking model returns the correct string representation	✅
test_menu_price	Ensures that the price field in the Menu model stores correct decimal values	✅
Serializers
Test Case	Description	Status
test_valid_menu_serializer	Verifies that valid data can be serialized correctly using MenuSerializer	✅
test_invalid_menu_serializer	Verifies that invalid data (missing required fields) will cause serialization to fail	✅
test_valid_booking_serializer	Verifies that valid data can be serialized correctly using BookingSerializer	✅
Views
Test Case	Description	Status
test_list_users_authenticated	Verifies that an authenticated user can view the list of users	✅
test_list_users_unauthenticated	Ensures that unauthenticated requests to list users are blocked	✅
test_create_menu_item	Verifies that a new menu item can be successfully created	✅
test_list_menu_items	Verifies that menu items are listed correctly	✅
test_list_bookings	Ensures that the list of bookings is displayed correctly	✅
test_create_booking	Verifies that a new booking can be created successfully	✅
Legend: ✅ = Pass, ❌ = Fail
This summary updates automatically based on test runs.
