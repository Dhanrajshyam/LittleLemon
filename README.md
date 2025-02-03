# 🍋 Little Lemon

Welcome to **Little Lemon**, a Django-based web application designed to manage and enhance restaurant operations. This project is part of the **Meta Back-End Developer Capstone** course and showcases essential backend development skills, including authentication, database management, and API integration.

---
![Django Tests](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/actions/workflows/tests.yml/badge.svg)
![Django Tests](https://github.com/Dhanrajshyam/LittleLemon/blob/main/.github/workflows/test.yml/badge.svg)
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

| Endpoint              | Method | Description                |
| --------------------- | ------ | -------------------------- |
| `/api/menu/`          | GET    | Fetch all menu items       |
| `/api/menu/<id>/`     | GET    | Fetch a specific menu item |
| `/api/reservations/`  | POST   | Make a table reservation   |
| `/api/auth/login/`    | POST   | User login                 |
| `/api/auth/register/` | POST   | User registration          |

---

## 📂 Project Structure

```
LittleLemon/
│-- manage.py
│-- littlelemon/  # Main app
│   │-- settings.py
│   │-- urls.py
│   │-- views.py
│-- reservations/  # Reservation system
│-- menu/  # Menu management
│-- users/  # Authentication system
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

