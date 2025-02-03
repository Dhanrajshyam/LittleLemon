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
| `/api/users` | GET | Handles user-related operations. |
| `/api/users` | POST | Handles user-related operations. |
| `/api/users` | PUT | Handles user-related operations. |
| `/api/users` | PATCH | Handles user-related operations. |
| `/api/users` | DELETE | Handles user-related operations. |
| `/api/users` | HEAD | Handles user-related operations. |
| `/api/users` | TRACE | Handles user-related operations. |
| `/api/users/<id>` | GET | Description |
| `/api/users/<id>` | POST | Description |
| `/api/users/<id>` | PUT | Description |
| `/api/users/<id>` | PATCH | Description |
| `/api/users/<id>` | DELETE | Delete a user by ID |
| `/api/users/<id>.<format>` | GET | Description |
| `/api/users/<id>.<format>` | POST | Description |
| `/api/users/<id>.<format>` | PUT | Description |
| `/api/users/<id>.<format>` | PATCH | Description |
| `/api/users/<id>.<format>` | DELETE | Delete a user by ID |
| `/api/users/.<format>` | GET | Handles user-related operations. |
| `/api/users/.<format>` | POST | Handles user-related operations. |
| `/api/users/.<format>` | PUT | Handles user-related operations. |
| `/api/users/.<format>` | PATCH | Handles user-related operations. |
| `/api/users/.<format>` | DELETE | Handles user-related operations. |
| `/api/menu` | GET | Handles menu-related operations. |
| `/api/menu` | POST | Handles menu-related operations. |
| `/api/menu` | PUT | Handles menu-related operations. |
| `/api/menu` | PATCH | Handles menu-related operations. |
| `/api/menu` | DELETE | Handles menu-related operations. |
| `/api/menu` | HEAD | Handles menu-related operations. |
| `/api/menu` | TRACE | Handles menu-related operations. |
| `/api/menu/<id>` | GET | Description |
| `/api/menu/<id>` | POST | Description |
| `/api/menu/<id>` | PUT | Description |
| `/api/menu/<id>` | PATCH | Description |
| `/api/menu/<id>` | DELETE | Description |
| `/api/menu/<id>.<format>` | GET | Description |
| `/api/menu/<id>.<format>` | POST | Description |
| `/api/menu/<id>.<format>` | PUT | Description |
| `/api/menu/<id>.<format>` | PATCH | Description |
| `/api/menu/<id>.<format>` | DELETE | Description |
| `/api/menu/.<format>` | GET | Handles menu-related operations. |
| `/api/menu/.<format>` | POST | Handles menu-related operations. |
| `/api/menu/.<format>` | PUT | Handles menu-related operations. |
| `/api/menu/.<format>` | PATCH | Handles menu-related operations. |
| `/api/menu/.<format>` | DELETE | Handles menu-related operations. |
| `/api/booking` | GET | Handles booking-related operations. |
| `/api/booking` | POST | Handles booking-related operations. |
| `/api/booking` | PUT | Handles booking-related operations. |
| `/api/booking` | PATCH | Handles booking-related operations. |
| `/api/booking` | DELETE | Handles booking-related operations. |
| `/api/booking` | HEAD | Handles booking-related operations. |
| `/api/booking` | TRACE | Handles booking-related operations. |
| `/api/booking/<id>` | GET | Description |
| `/api/booking/<id>` | POST | Description |
| `/api/booking/<id>` | PUT | Description |
| `/api/booking/<id>` | PATCH | Description |
| `/api/booking/<id>` | DELETE | Description |
| `/api/booking/<id>.<format>` | GET | Description |
| `/api/booking/<id>.<format>` | POST | Description |
| `/api/booking/<id>.<format>` | PUT | Description |
| `/api/booking/<id>.<format>` | PATCH | Description |
| `/api/booking/<id>.<format>` | DELETE | Description |
| `/api/booking/.<format>` | GET | Handles booking-related operations. |
| `/api/booking/.<format>` | POST | Handles booking-related operations. |
| `/api/booking/.<format>` | PUT | Handles booking-related operations. |
| `/api/booking/.<format>` | PATCH | Handles booking-related operations. |
| `/api/booking/.<format>` | DELETE | Handles booking-related operations. |

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