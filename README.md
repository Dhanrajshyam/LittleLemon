# 🍋 Little Lemon

Welcome to **Little Lemon**, a Django-based web application designed to manage and enhance restaurant operations. This project is part of the **Meta Back-End Developer Capstone** course and showcases essential backend development skills, including authentication, database management, and API integration.

---

## 📌 Features

- 🛠 **Django Framework**: Built using Django for a robust and scalable backend.
- 🔐 **User Authentication**: Secure user login and registration.
- 📊 **Database Management**: Utilizes SQLite/MySQL for efficient data storage.
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

### **3. Install Dependencies**

```sh
 pip install -r requirements.txt
```

### **4. Run Database Migrations**

```sh
 python manage.py makemigrations
 python manage.py migrate
```

### **5. Create a Superuser (Admin Access)**

```sh
 python manage.py createsuperuser
```

### **6. Start the Development Server**

```sh
 python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---


## 🔗 API Endpoints

|   Name   | API Endpoint | Http Method | Available Format | Description |
| -------- | ------------ | ----------- | ---------------- | ----------- |
|**home**|`^\Z`|get|html|Homepage of the application|
|**user-list**|`^api/^users$`|get|json,api,xml,csv|Retrieve a list of users|
||`^api/^users$`|post|json,api,xml,csv|Create a new user|
||`^api/^users\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a list of users|
||`^api/^users\.(?P<format>[a-z0-9]+)/?$`|post|json,api,xml,csv|Create a new user|
|**user-detail**|`^api/^users/(?P<pk>[^/.]+)$`|get|json,api,xml,csv|Retrieve a user by ID|
||`^api/^users/(?P<pk>[^/.]+)$`|put|json,api,xml,csv|Update a user by ID|
||`^api/^users/(?P<pk>[^/.]+)$`|patch|json,api,xml,csv|Partially update a user by ID|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|get|json,api,xml,csv|Retrieve a user by ID|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|put|json,api,xml,csv|Update a user by ID|
||`^api/^users/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$`|patch|json,api,xml,csv|Partially update a user by ID|
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
|**login**|`^api\-auth/^login/\Z`|get|html|Display the login form and handle the login action.|
|**logout**|`^api\-auth/^logout/\Z`|get|html|Log out the user and display the 'You are logged out' message.|

## 📂 Project Structure

```
📦LittleLemon
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃ ┃ ┣ 📜codeql.yml
 ┃ ┃ ┣ 📜dependency-review.yml
 ┃ ┃ ┗ 📜test.yml
 ┣ 📂Littlelemon
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜wsgi.py
 ┃ ┗ 📜__init__.py
 ┣ 📂Restaurant
 ┃ ┣ 📂static
 ┃ ┃ ┣ 📂css
 ┃ ┃ ┃ ┗ 📜style.css
 ┃ ┃ ┗ 📂img
 ┃ ┃ ┃ ┣ 📜Bruschetta.jpg
 ┃ ┃ ┃ ┣ 📜favicon.ico
 ┃ ┃ ┃ ┣ 📜greek salad.jpg
 ┃ ┃ ┃ ┣ 📜Grill B.jpg
 ┃ ┃ ┃ ┣ 📜Grill.jpg
 ┃ ┃ ┃ ┣ 📜Grilled fish B.jpg
 ┃ ┃ ┃ ┣ 📜Grilled fish C.jpg
 ┃ ┃ ┃ ┣ 📜Grilled fish.jpg
 ┃ ┃ ┃ ┣ 📜head_chef.jpg
 ┃ ┃ ┃ ┣ 📜lemon dessert B.jpg
 ┃ ┃ ┃ ┣ 📜lemon dessert.jpg
 ┃ ┃ ┃ ┣ 📜logo.png
 ┃ ┃ ┃ ┣ 📜logo_footer.png
 ┃ ┃ ┃ ┣ 📜Mario and Adrian b.jpg
 ┃ ┃ ┃ ┣ 📜mario-and-adrian.jpg
 ┃ ┃ ┃ ┣ 📜pasta.jpg
 ┃ ┃ ┃ ┣ 📜restaurant chef C.jpg
 ┃ ┃ ┃ ┣ 📜restaurant food B.jpg
 ┃ ┃ ┃ ┣ 📜restaurant food.jpg
 ┃ ┃ ┃ ┣ 📜restaurant inside alternative.jpg
 ┃ ┃ ┃ ┣ 📜restaurant_inside.jpg
 ┃ ┃ ┃ ┗ 📜salad.jpg
 ┃ ┣ 📂tests
 ┃ ┃ ┣ 📜test_models.py
 ┃ ┃ ┣ 📜test_serializers.py
 ┃ ┃ ┣ 📜test_views.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜urls.py
 ┃ ┣ 📜views.py
 ┃ ┗ 📜__init__.py
 ┣ 📂templates
 ┃ ┗ 📜index.html
 ┣ 📜.env
 ┣ 📜.gitignore
 ┣ 📜db.sqlite3
 ┣ 📜manage.py
 ┣ 📜Pipfile
 ┣ 📜Pipfile.lock
 ┣ 📜pytest.ini
 ┣ 📜README.md
 ┣ 📜requirements.txt
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