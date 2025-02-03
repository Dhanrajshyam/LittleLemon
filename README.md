# 🍋 Little Lemon

Welcome to **Little Lemon**, a Django-based web application designed to manage and enhance restaurant operations. This project is part of the **Meta Back-End Developer Capstone** course and showcases essential backend development skills, including authentication, database management, and API integration.

---

## 📌 Features

- 🛠 **Django Framework**: Built using Django for a robust and scalable backend.
- 🔐 **User Authentication**: Secure user login and registration.
- 📊 **Database Management**: Utilizes SQLite/PostgreSQL for efficient data storage.
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

| Endpoint | Method | Description |
| -------- | ------ | ----------- |
| `\Z` | GET, POST | Description |
| `^api/users` | GET, POST | Description |
| `^api/users\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/users/(?P<pk>[/.]+)` | GET, POST | Description |
| `^api/users/(?P<pk>[/.]+)\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/menu` | GET, POST | Description |
| `^api/menu\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/menu/(?P<pk>[/.]+)` | GET, POST | Description |
| `^api/menu/(?P<pk>[/.]+)\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/booking` | GET, POST | Description |
| `^api/booking\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/booking/(?P<pk>[/.]+)` | GET, POST | Description |
| `^api/booking/(?P<pk>[/.]+)\.(?P<format>[a-z0-9]+)/?` | GET, POST | Description |
| `^api/\Z` | get, post, put, patch, delete, head, options, trace | Description |
| `^api/(?P<format>\.[a-z0-9]+/?)\Z` | get, post, put, patch, delete, head, options, trace | Description |
---| `^api\-auth/login/\Z` | get, post, put, patch, delete, head, options, trace | Description |
| `^api\-auth/logout/\Z` | post, options | Description |
------
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