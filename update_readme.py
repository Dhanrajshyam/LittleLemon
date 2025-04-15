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

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

# Readme file
README_FILE = "README.md"

MARKDOWN_STATIC_CONTENT = r"""
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

"""


API_ENDPOINTS_RESTRICTIONS = r"""
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
- Normal users(Authenticated) can view the list of bookings booked by them and its booking details.
- Anonymous (Unauthenticated) Users can't access the booking API endpoints.

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
{API_ENDPOINTS_RESTRICTIONS}
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
