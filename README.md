# 🍋 Little Lemon

Welcome to **Little Lemon**, a Django-based web application designed to manage and enhance restaurant operations. This project is part of the **Meta Back-End Developer Capstone** course and showcases essential backend development skills, including authentication, database management, and API integration.

---

## 📌 Features

- 🛠 **Django Framework**: Built using Django for a robust and scalable backend.
- 🔐 **User Authentication**: Secure user login and registration.
- 📊 **Database Management**: Utilizes SQLite/MySQL/PostgreSQL for efficient data storage.
- 📡 **RESTful API**: Implements Django REST Framework (DRF) for API endpoints.
- 📅 **Reservation System**: Allows customers to book tables online.
- 🛒 **Menu Management**: Enables easy updates to the restaurant menu.

---

## 🚀 Installation & Setup

### **1. Clone the Repository**

```sh
 git clone https://github.com/Dhanrajshyam/LittleLemon.git
 cd LittleLemon
```

### **2. Create a Virtual Environment & Activate It**

```sh
 python -m venv venv  # Create virtual environment
 source venv/bin/activate  # MacOS/Linux
 venv\Scripts\activate  # Windows
```
- Alternatively you can use pipenv to create a virtual environment.

### **3. Install Dependencies**

```sh
 pip install -r requirements.txt
```

### **4. Run Database Migrations**

- Ensure you have installed PostgreSQL or MySQL on your system.
- Update the database settings in the `settings.py` file.
    - Update Database Engine, Name, User, Password, Port and Host.
- Ensure you are in the project directory where the `manage.py` file is located.

```sh
 python manage.py makemigrations
 python manage.py migrate
```

### **5. Create a Superuser (Admin Access)**

```sh
 python manage.py createsuperuser
```
- This will be used to verify updates made on web application and API endpoints are reflected in database model using Admin Panel.

### **6. Start the Development Server**

```sh
 python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

### **7. Create Branch_Manager Group and Add User to Branch_Manager Group** - Optional

- Visit `http://127.0.0.1:8000/admin` in your browser.
- Login with the superuser credentials created earlier.
- Create a new group named `Branch_Manager` in `Groups` section.
- Add a user to the `Branch_Manager` group in the `Users` section.
    - User with Branch_Manager group will have access to all users data.
    - Normal users will have access to only their data.

---


## 🔗 API Endpoints

|   Name   | API Endpoint | Http Method | Available Format | Description |
| -------- | ------------ | ----------- | ---------------- | ----------- |
|**home**|`^\Z`|get|html|Homepage of the application|
|**customuser-list**|`^api/^users$`|get|json,api,xml,csv|Retrieve a list of users|
||`^api/^users$`|post|json,api,xml,csv|Create a new user|
||`^api/^users\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a list of users|
||`^api/^users\.(?P<format>[a-z0-9]+)/?$`|post|json,api,xml,csv|Create a new user|
|**customuser-detail**|`^api/^users/(?P<pk>[^/.]+)$`|get|json,api,xml,csv|Retrieve a user|
||`^api/^users/(?P<pk>[^/.]+)$`|put|json,api,xml,csv|Update a user|
||`^api/^users/(?P<pk>[^/.]+)$`|patch|json,api,xml,csv|Partially update a user|
||`^api/^users/(?P<pk>[^/.]+)$`|delete|json,api,xml,csv|Delete a user|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a user|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|put|json,api,xml,csv|Update a user|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|patch|json,api,xml,csv|Partially update a user|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|delete|json,api,xml,csv|Delete a user|
|**menu-list**|`^api/^menu$`|get|json,api,xml,csv|Retrieve a list of menu items|
||`^api/^menu$`|post|json,api,xml,csv|Create a new menu|
||`^api/^menu\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a list of menu items|
||`^api/^menu\.(?P<format>[a-z0-9]+)/?$`|post|json,api,xml,csv|Create a new menu|
|**menu-detail**|`^api/^menu/(?P<pk>[^/.]+)$`|get|json,api,xml,csv|Retrieve a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)$`|put|json,api,xml,csv|Update a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)$`|patch|json,api,xml,csv|Partially update a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)$`|delete|json,api,xml,csv|Delete a menu by ID|
||`^api/^menu/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|put|json,api,xml,csv|Update a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|patch|json,api,xml,csv|Partially update a menu item by ID|
||`^api/^menu/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|delete|json,api,xml,csv|Delete a menu by ID|
|**booking-list**|`^api/^booking$`|get|json,api,xml,csv|Retrieve a list of bookings|
||`^api/^booking$`|post|json,api,xml,csv|Create a new booking|
||`^api/^booking\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a list of bookings|
||`^api/^booking\.(?P<format>[a-z0-9]+)/?$`|post|json,api,xml,csv|Create a new booking|
|**booking-detail**|`^api/^booking/(?P<pk>[^/.]+)$`|get|json,api,xml,csv|Retrieve a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)$`|put|json,api,xml,csv|Update a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)$`|patch|json,api,xml,csv|Partially update a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)$`|delete|json,api,xml,csv|Delete a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|put|json,api,xml,csv|Update a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|patch|json,api,xml,csv|Partially update a booking by ID|
||`^api/^booking/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|delete|json,api,xml,csv|Delete a booking by ID|
|**api-root**|`^api/^\Z`|get|html|The default basic root view for DefaultRouter|
||`^api/^(?P<format>\.[a-z0-9]+/?)\Z`|get|html|The default basic root view for DefaultRouter|
|**user_sign_up**|`^user/sign_up/\Z`|get|html|Sign up a new user|
|**terms_n_conditions**|`^terms/\Z`|get|html|Terms and conditions page|
|**login**|`^login/\Z`|get|html|Login the user|
|**logout**|`^logout/\Z`|get|html|Logout the user|


---
# API Endpoints Restrictions

## User API Endpoints
- Users with Branch_Manager group can perform all CRUD operations on all users.
- Normal users can view their own profile/account details and perform update/delete(account deletion) on it. 

## Menu API Endpoints
- Users with Branch_Manager group can perform all CRUD operations on all menu items.
- Normal users can view the list of menu items and indivisual menu item details.

## Booking API Endpoints
- Users with Branch_Manager group can perform all CRUD operations on all booking by all users.
- Normal users can view the list of bookings booked by them and its booking details.

---

## 📂 Project Structure

```
📦LittleLemon
 ┣ 📂docs
 ┃ ┣ 📂design
 ┃ ┃ ┣ 📂draft_ideas
 ┃ ┃ ┃ ┣ 📜Complete Django Authentication_MFA Implementation.md
 ┃ ┃ ┃ ┣ 📜Complete Django Authentication_MFA Implementation_V2.md
 ┃ ┃ ┃ ┣ 📜Comprehensive Authentication_Security_Deployment Setup.md
 ┃ ┃ ┃ ┣ 📜Django Authentication and Security Setup.md
 ┃ ┃ ┃ ┗ 📜Django_Authentication_MFA_Setup.md
 ┃ ┃ ┣ 📂guidelines
 ┃ ┃ ┣ 📂UI
 ┃ ┃ ┃ ┗ 📜littlelemonUI.md
 ┃ ┃ ┗ 📜DESIGN.md
 ┃ ┣ 📂dev
 ┃ ┃ ┗ 📂guidelines
 ┃ ┃ ┃ ┣ 📜Branch_Merge_Delete_Strategy.md
 ┃ ┃ ┃ ┣ 📜project_guidelines.md
 ┃ ┃ ┃ ┣ 📜project_setup_guidelines_local.md
 ┃ ┃ ┃ ┗ 📜Version_Control_guidelines.md
 ┃ ┗ 📂project_management
 ┃ ┃ ┗ 📂Release 1.0.0
 ┃ ┃ ┃ ┣ 📂others
 ┃ ┃ ┃ ┃ ┣ 📜ISSUES_TEMPLATE.md
 ┃ ┃ ┃ ┃ ┣ 📜RELEASE_TEMPLATE.md
 ┃ ┃ ┃ ┃ ┗ 📜SPRINT_TEMPLATE.md
 ┃ ┃ ┃ ┣ 📜EPIC.md
 ┃ ┃ ┃ ┣ 📜FEATURES.md
 ┃ ┃ ┃ ┣ 📜ROADMAP.md
 ┃ ┃ ┃ ┣ 📜TASKS.md
 ┃ ┃ ┃ ┗ 📜USER_STORIES.md
 ┃ ┣ 📜.gitignore
 ┃ ┗ 📜pyvenv.cfg
 ┣ 📂Littlelemon
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂Restaurant
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📜test_forms.py
 ┃ ┃ ┣ 📜test_models.py
 ┃ ┃ ┣ 📜test_serializers.py
 ┃ ┃ ┣ 📜test_views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜forms.py
 ┃ ┣ 📜managers.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜utils.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂bootstrap
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📜bootstrap.min.css
 ┃ ┃ ┗ 📂js
 ┃ ┃ ┃ ┗ 📜bootstrap.min.js
 ┃ ┣ 📂css
 ┃ ┃ ┣ 📜animate.min.css
 ┃ ┃ ┣ 📜bs-theme-overrides.css
 ┃ ┃ ┣ 📜Login-Form-Basic-icons.css
 ┃ ┃ ┣ 📜mobile_navbar.css
 ┃ ┃ ┗ 📜styles.css
 ┃ ┣ 📂img
 ┃ ┃ ┣ 📂chefs
 ┃ ┃ ┃ ┣ 📜head_chef.jpg
 ┃ ┃ ┃ ┣ 📜Mario and Adrian b.jpg
 ┃ ┃ ┃ ┣ 📜mario-and-adrian.jpg
 ┃ ┃ ┃ ┗ 📜restaurant chef C.jpg
 ┃ ┃ ┣ 📂icon
 ┃ ┃ ┃ ┣ 📜android-chrome-192x192.png
 ┃ ┃ ┃ ┣ 📜android-chrome-512x512.png
 ┃ ┃ ┃ ┣ 📜apple-touch-icon.png
 ┃ ┃ ┃ ┣ 📜favicon-16x16.png
 ┃ ┃ ┃ ┣ 📜favicon-32x32.png
 ┃ ┃ ┃ ┗ 📜favicon.ico
 ┃ ┃ ┣ 📂logo
 ┃ ┃ ┃ ┣ 📜Brand Logo Dark.png
 ┃ ┃ ┃ ┣ 📜Brand Logo White.png
 ┃ ┃ ┃ ┣ 📜Brand_Logo_wobg_shadow.png
 ┃ ┃ ┃ ┣ 📜Brand_Logo_wobkg.png
 ┃ ┃ ┃ ┣ 📜Little_Lemon_Horizontal-wobg.png
 ┃ ┃ ┃ ┣ 📜Logo Dark.png
 ┃ ┃ ┃ ┗ 📜Logo White.png
 ┃ ┃ ┣ 📂lottie
 ┃ ┃ ┃ ┗ 📜404.lottie
 ┃ ┃ ┣ 📂menu
 ┃ ┃ ┃ ┣ 📜Bruschetta.jpg
 ┃ ┃ ┃ ┣ 📜greek_salad.jpg
 ┃ ┃ ┃ ┣ 📜Grill.jpg
 ┃ ┃ ┃ ┣ 📜Grilled_fish.jpg
 ┃ ┃ ┃ ┣ 📜Grilled_fish_B.jpg
 ┃ ┃ ┃ ┣ 📜Grilled_fish_C.jpg
 ┃ ┃ ┃ ┣ 📜Grill_B.jpg
 ┃ ┃ ┃ ┣ 📜lemon_dessert.jpg
 ┃ ┃ ┃ ┣ 📜lemon_dessert_B.jpg
 ┃ ┃ ┃ ┣ 📜pasta.jpg
 ┃ ┃ ┃ ┗ 📜salad.jpg
 ┃ ┃ ┗ 📂photos
 ┃ ┃ ┃ ┣ 📜restaurant food.jpg
 ┃ ┃ ┃ ┣ 📜restaurant inside alternative.jpg
 ┃ ┃ ┃ ┣ 📜restaurant_food B.jpg
 ┃ ┃ ┃ ┣ 📜restaurant_food.jpg
 ┃ ┃ ┃ ┗ 📜restaurant_inside.jpg
 ┃ ┗ 📂js
 ┃ ┃ ┣ 📜bs-init.js
 ┃ ┃ ┣ 📜littlelemon_main.js
 ┃ ┃ ┣ 📜sign_up.js
 ┃ ┃ ┗ 📜theme-toggle.js
 ┣ 📂templates
 ┃ ┣ 📂partials
 ┃ ┃ ┣ 📜_footer.html
 ┃ ┃ ┗ 📜_header.html
 ┃ ┣ 📜404.html
 ┃ ┣ 📜base.html
 ┃ ┣ 📜index.html
 ┃ ┣ 📜login.html
 ┃ ┣ 📜sign_up_success.html
 ┃ ┣ 📜terms_n_conditions.html
 ┃ ┗ 📜user_sign_up.html
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜CODE_OF_CONDUCT.md
 ┣ 📜CONTRIBUTING.md
 ┣ 📜db.sqlite3
 ┣ 📜LICENSE
 ┣ 📜manage.py
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜pytest.ini
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┣ 📜sample.py
 ┣ 📜SECURITY.md
 ┣ 📜speedometer.svg
 ┣ 📜TEST_RESULTS.md
 ┣ 📜update_readme.py
 ┗ 📜update_test_results.py
```


---

## 📜 License

This project is for educational purposes as part of the **Meta Back-End Developer Capstone** course.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to contribute to this project by improving features, fixing bugs, or enhancing documentation.

---

## 📞 Contact

For questions or collaborations, reach out via GitHub Issues.

🚀 Happy coding!