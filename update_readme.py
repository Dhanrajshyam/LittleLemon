
import django
import os
# Django settings setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Littlelemon.settings")
django.setup()

from Restaurant.urls import urlpatterns
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# # Django settings setup
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Littlelemon.settings")
# django.setup()

# Readme file
README_FILE = "README.md"

MARKDOWN_STATIC_CONTENT = r"""
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

"""

MARKDOWN_FOOTER = r"""
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
"""

PROJECT_TREE = r"""
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
"""


def generate_api_enpoints(url_patterns):
    markdown_content = "## 🔗 API Endpoints\n\n"
    markdown_content += "| Endpoint | Method | Description |\n"
    markdown_content += "| -------- | ------ | ----------- |\n"

    def process_urlpatterns(patterns, base_url=""):
        nonlocal markdown_content
        for pattern in patterns:
            if hasattr(pattern, 'url_patterns'):
                # This is an include() directive
                process_urlpatterns(pattern.url_patterns, base_url + pattern.pattern.regex.pattern)
            else:
                endpoint = base_url + pattern.pattern.regex.pattern.replace('^', '').replace('$', '')
                if hasattr(pattern.callback, 'view_class'): 
                    methods = ", ".join(pattern.callback.view_class().http_method_names)
                else: 
                    methods = "GET, POST" 
                # For simplicity, the description is left blank
                markdown_content += f"| `{endpoint}` | {methods} | Description |\n"
        markdown_content += "---"
    process_urlpatterns(url_patterns)
    return markdown_content


def generate_update_markdown(file, header, footer, project_path, api_urls):
    api_enpoints = generate_api_enpoints(api_urls)
    project_tree = project_path
    markdown = f"""
{header}
{api_enpoints}
## 📂 Project Structure
{project_tree}
{footer}
    """

    with open(file, "w+", encoding="utf-8") as f:
        f.write(markdown.strip())

# Main function to execute the script


def main():
    generate_update_markdown(
        README_FILE, MARKDOWN_STATIC_CONTENT, MARKDOWN_FOOTER, PROJECT_TREE, urlpatterns)
    print(f"✅ {README_FILE} updated successfully!")


if __name__ == "__main__":
    main()
