import django
import os
# Django settings setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Littlelemon.settings")
django.setup()

from Restaurant.urls import urlpatterns as app_urls
import importlib
from django.conf import settings
from Restaurant.views import UserViewSet, MenuViewSet, BookingViewSet
from django.urls.resolvers import URLPattern, URLResolver


from Restaurant.urls import router  # Import your router
from collections import defaultdict
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


def get_docstring_from_lookup_string(lookup_str, function_name = None):
    # Split the lookup string to get the module and class names
    components = lookup_str.split('.')
    
    # Import the module dynamically
    module_name = '.'.join(components[:-1])
    module = importlib.import_module(module_name)
    
    # Get the class (or function) from the module
    obj_name = components[-1]
    obj = getattr(module, obj_name)
    if function_name is not None:
        obj = getattr(obj, function_name)
    
    # Retrieve the docstring
    docstring = obj.__doc__
    
    return docstring

def get_formats_from_view(view):
    renderers = []

    if isinstance(view, (UserViewSet, MenuViewSet, BookingViewSet)):
        view_class = view.cls if hasattr(view, 'cls') else view.__class__
        renderers = view_class.renderer_classes
    elif hasattr(view, 'cls') and hasattr(view.cls, 'renderer_classes'):
        renderers = view.cls.renderer_classes
    elif hasattr(view, 'renderer_classes'):
        renderers = view.renderer_classes
    elif hasattr(view, '__func__'):
        func = view.__func__
        if hasattr(func, 'renderer_classes'):
            renderers = func.renderer_classes
    else:
        # Use the default renderer classes if no specific renderers are found
        renderers = settings.REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']
    
    formats = [renderer.format for renderer in renderers]
    return formats


def get_endpoint_from_urlpattern(url_pattern, base_route = ''):
    if isinstance(url_pattern, URLPattern):
        endpoints = []
        pattern_name = url_pattern.name
        api_endpoint = base_route + url_pattern.pattern._regex
        http_method = 'get'
        description = url_pattern.callback.__doc__
        description = description.strip()
        module_name = url_pattern.callback.__module__
        function_name = url_pattern.callback.__name__
        available_format = 'html'
        
        callback_func = url_pattern.callback
        if hasattr(callback_func, "actions"):
            for key, value in callback_func.actions.items():
                http_method = key
                function_name = value
                module_name = url_pattern.lookup_str
                description = get_docstring_from_lookup_string(module_name, function_name).strip()
                available_format = get_formats_from_view(callback_func.cls if hasattr(callback_func, 'cls') else callback_func)
                available_format = ",".join(available_format)
                # "|   Name   | API Endpoint | Http Method | Available Format | Description |\n"
                endpoint = [pattern_name, api_endpoint, http_method, available_format, description, module_name, function_name]
                endpoints.append(endpoint)
        else:
            endpoint = [pattern_name, api_endpoint, http_method, available_format, description, module_name, function_name]
            endpoints.append(endpoint)
    
        return endpoints
    else:
        return []

def get_endpoints_from_urlresolver(url_pattern):
    if isinstance(url_pattern, URLResolver):
        result_endpoints = []
        base_route = url_pattern.pattern._regex
        for pattern in url_pattern.url_patterns:
            endpoints = get_endpoint_from_urlpattern(pattern, base_route)
            result_endpoints.extend(endpoints)
        return result_endpoints
    else:
        endpoints = get_endpoint_from_urlpattern(url_pattern)
        return endpoints

def convert_list_to_markdown(api_endpoint_list):
    markdown_content = "## 🔗 API Endpoints\n\n"
    markdown_content += "|   Name   | API Endpoint | Http Method | Available Format | Description |\n"
    markdown_content += "| -------- | ------------ | ----------- | ---------------- | ----------- |\n"
    previous = ''
    for endpoint in api_endpoint_list:
        if previous == endpoint[0]:
            endpoint[0] = ''
        else:
            previous = endpoint[0]
            endpoint[0] = f"**{endpoint[0]}**"
        endpoint[1] = f"`{endpoint[1]}`"
        markdown_content += '|' + "|".join(endpoint[0:5]) + "|\n"
    return markdown_content


def generate_readme_markdown(file, header, footer, project_path, urls):
    api_enpoints = []
    for pattern in urls:
        endpoints = get_endpoints_from_urlresolver(pattern)
        api_enpoints.extend(endpoints)
    api_endpoints_markdown = convert_list_to_markdown(api_enpoints)
    project_tree = project_path
    markdown = f"""
{header}
{api_endpoints_markdown}
## 📂 Project Structure
{project_tree}
{footer}
    """

    with open(file, "w+", encoding="utf-8") as f:
        f.write(markdown.strip())

# Main function to execute the script


def main():
    generate_readme_markdown(
        README_FILE, MARKDOWN_STATIC_CONTENT, MARKDOWN_FOOTER, PROJECT_TREE, app_urls)
    print(f"✅ {README_FILE} updated successfully!")


if __name__ == "__main__":
    main()
