# 🚀 Installation & Setup

## **1. Clone the Repository**

```sh
 git clone https://github.com/Dhanrajshyam/LittleLemon.git
 cd LittleLemon
```

## **2. Create a Virtual Environment & Activate It**

```sh
 python -m venv venv  # Create virtual environment
 source venv/bin/activate  # MacOS/Linux
 venv\Scripts\activate  # Windows
```

## **3. Install Dependencies**

```sh
 pip install -r requirements.txt
```

## **4. Run Database Migrations**

- Goto `LittleLemon/Littlelemon` directory and update the `settings.py` file with your database credentials.
```sh
 python manage.py makemigrations
 python manage.py migrate
```

## **5. Create a Superuser (Admin Access)**

```sh
 python manage.py createsuperuser
```

## **6. Start the Development Server**

```sh
 python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.