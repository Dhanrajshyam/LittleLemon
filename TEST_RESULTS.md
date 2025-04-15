# 🛠 Django Test Results

![Overall Status](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml/badge.svg)

This file documents all the test cases executed in the Django project and their latest execution status in GitHub Actions.

---

### 📝 Test Progress

![Test Speedometer](speedometer.svg)

---

### 📝 Test Case Summary
#### ![Test Coverage](https://img.shields.io/badge/Tests-✅_100%25_Passed-green)

- **Total Test Cases:** 🧪 `48`
- **Passed:** ✅ `48`
- **Failed:** ❌ `0`


            
#### Models
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_booking_str` | Test string representation of Booking model | ✅PASS |
| `test_create_superuser_success` | Test creating a superuser. | ✅PASS |
| `test_create_user_success` | Test creating a user with email and password. | ✅PASS |
| `test_create_user_without_email_fails` | Test that creating a user without an email raises an error. | ✅PASS |
| `test_phone_number_invalid_length` | Test that an invalid phone number raises a validation error. | ✅PASS |
| `test_phone_number_validation` | Test that phone number must be exactly 10 digits. | ✅PASS |
| `test_menu_price` | Ensure price is stored correctly | ✅PASS |
| `test_menu_str` | Test the string representation of Menu model | ✅PASS |
| `test_create_superuser` | No description available | ✅PASS |
| `test_create_user` | No description available | ✅PASS |

#### Serializers
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_invalid_booking_serializer` | Test serializer with invalid guest number | ✅PASS |
| `test_valid_booking_serializer` | Test serializer with valid data | ✅PASS |
| `test_invalid_menu_serializer` | Test serializer with missing fields | ✅PASS |
| `test_valid_menu_serializer` | Test serializer with valid data | ✅PASS |
| `test_user_serializer_invalid_email` | Test deserialization with invalid email | ✅PASS |
| `test_user_serializer_invalid_phone_number` | Test deserialization with invalid phone number format | ✅PASS |
| `test_user_serializer_optional_groups` | Test serializer behavior when groups are omitted | ✅PASS |
| `test_user_serializer_valid_data` | Test serialization of a user instance | ✅PASS |
| `test_user_serializer_valid_input` | Test deserialization with valid data | ✅PASS |

#### Views
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_create_booking` | Test creating a new booking. | ✅PASS |
| `test_create_booking_invalid_data` | Test creating a booking with invalid data. | ✅PASS |
| `test_delete_booking` | Test deleting a booking. | ✅PASS |
| `test_list_bookings` | Test retrieving a list of bookings. | ✅PASS |
| `test_partial_update_booking` | Test partially updating a booking. | ✅PASS |
| `test_retrieve_booking` | Test retrieving a specific booking by ID. | ✅PASS |
| `test_unauthenticated_access` | Test that unauthenticated users cannot access booking endpoints. | ✅PASS |
| `test_update_booking` | Test updating a booking. | ✅PASS |
| `test_create_menu` | Test creating a new menu item. | ✅PASS |
| `test_create_menu_invalid_data` | Test creating a menu item with invalid data. | ✅PASS |
| `test_delete_menu` | Test deleting a menu item. | ✅PASS |
| `test_list_menus` | Test retrieving a list of menu items. | ✅PASS |
| `test_partial_update_menu` | Test partially updating a menu item. | ✅PASS |
| `test_retrieve_menu` | Test retrieving a specific menu item by ID. | ✅PASS |
| `test_update_menu` | Test updating a menu item. | ✅PASS |
| `test_create_user` | Test user creation | ✅PASS |
| `test_delete_user` | Test deleting a user | ✅PASS |
| `test_list_users` | Test listing users | ✅PASS |
| `test_list_users_unauthenticated` | Unauthenticated request should not be authorised | ✅PASS |
| `test_partial_update_user` | Test partially updating a user | ✅PASS |
| `test_unauthenticated_user_access` | Ensure unauthenticated users cannot access user endpoints | ✅PASS |
| `test_update_user` | Test updating a user | ✅PASS |

#### Forms
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_invalid_phone_number` | Test form with invalid phone number (not 10 digits) | ✅PASS |
| `test_password_does_not_meet_criteria` | Test form with weak password (missing special character) | ✅PASS |
| `test_password_not_matching` | Test form when passwords do not match | ✅PASS |
| `test_valid_data` | Test form with valid data | ✅PASS |
| `test_invalid_email` | Test login form with invalid email format | ✅PASS |
| `test_missing_password` | Test login form with missing password | ✅PASS |
| `test_valid_login_form` | Test login form with valid data | ✅PASS |


**Legend**: ✅ = Pass, ❌ = Fail

This summary updates automatically based on test runs.

---

## 🔍 View Complete Test Logs:
[GitHub Actions Test Logs](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml)

---

## ✅ **How to Run Tests Locally**
Run the following command in your terminal to execute tests:
```bash
python manage.py test --keepdb
```
---

## 📢 How to Integrate This in Your Git Repo

Copy this file as `TEST_RESULTS.md` and place it in your repository root.

Commit & Push the file:
```bash
git add TEST_RESULTS.md
git commit -m "Added test results markdown file"
git push origin main
```