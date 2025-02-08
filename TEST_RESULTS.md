# 🛠 Django Test Results

![Overall Status](https://github.com/Dhanrajshyam/LittleLemon/actions/workflows/test.yml/badge.svg)

This file documents all the test cases executed in the Django project and their latest execution status in GitHub Actions.

---

### 📝 Test Progress

![Test Speedometer](speedometer.svg)

---

### 📝 Test Case Summary
#### ![Test Coverage](https://img.shields.io/badge/Tests-✅_100%25_Passed-green)

- **Total Test Cases:** 🧪 `13`
- **Passed:** ✅ `13`
- **Failed:** ❌ `0`


            
#### Models
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_booking_str` | Test string representation of Booking model | ✅PASS |
| `test_menu_price` | Ensure price is stored correctly | ✅PASS |
| `test_menu_str` | Test the string representation of Menu model | ✅PASS |

#### Serializers
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_invalid_booking_serializer` | Test serializer with invalid guest number | ✅PASS |
| `test_valid_booking_serializer` | Test serializer with valid data | ✅PASS |
| `test_invalid_menu_serializer` | Test serializer with missing fields | ✅PASS |
| `test_valid_menu_serializer` | Test serializer with valid data | ✅PASS |

#### Views
| Test Case | Description | Status |
| --------- | ----------- | ------ |
| `test_create_booking` | Test booking creation | ✅PASS |
| `test_list_bookings` | Test booking listing | ✅PASS |
| `test_create_menu_item` | Create a new menu item | ✅PASS |
| `test_list_menu_items` | Ensure menu items are listed correctly | ✅PASS |
| `test_list_users_authenticated` | Authenticated user should be able to list users | ✅PASS |
| `test_list_users_unauthenticated` | Unauthenticated request should not be authorised | ✅PASS |


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