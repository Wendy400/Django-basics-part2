# Django Project Setup Guide

A complete step-by-step guide to setting up a Django application from scratch—from creating a virtual environment to wiring up views, templates, and URL routing.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Setting Up the Virtual Environment](#1-setting-up-the-virtual-environment)
3. [Installing Django & Creating the Project](#2-installing-django--creating-the-project)
4. [Creating a Django App](#3-creating-a-django-app)
5. [Configuring Installed Apps](#4-configuring-installed-apps)
6. [Creating Views](#5-creating-views)
7. [Setting Up Templates](#6-setting-up-templates)
8. [Wiring Up URL Routing](#7-wiring-up-url-routing)
9. [Running the Development Server](#8-running-the-development-server)
10. [Troubleshooting & Quick Commands](#9-troubleshooting--quick-commands)

---

## Prerequisites

Before starting, ensure you have Python installed on your system.

Check your Python version:
```bash
python --version
# or on macOS/Linux:
python3 --version
```

---

## 1. Setting Up the Virtual Environment

A virtual environment isolates project dependencies, preventing conflicts between package versions across different projects.

### Step 1.1: Navigate to Your Project Directory
Open your terminal or command prompt and navigate to the directory where you want your project to live:

```bash
# Windows / macOS / Linux
cd path/to/your/projects-folder
```

### Step 1.2: Create the Virtual Environment
Run the `venv` module to create an environment named `env` (or any name you prefer, e.g., `venv`, `Shop1`):

```bash
# Windows / macOS / Linux
python -m venv env
```

### Step 1.3: Activate the Virtual Environment

* **Windows (Command Prompt):**
  ```cmd
  env\Scripts\activate
  ```

* **Windows (PowerShell):**
  ```powershell
  .\env\Scripts\Activate.ps1
  ```

* **macOS / Linux:**
  ```bash
  source env/bin/activate
  ```

Once activated, your terminal prompt will show the environment name in parentheses, like `(env) C:\path\to\project>`.

---

## 2. Installing Django & Creating the Project

### Step 2.1: Upgrade `pip` and Install Django
Inside your active virtual environment, install Django:

```bash
pip install --upgrade pip
pip install django
```

Verify the installation:
```bash
python -m django --version
```

### Step 2.2: Create a New Django Project
Run `django-admin startproject` followed by your project name. Adding a `.` at the end creates the project in the current directory without creating an extra nested folder.

```bash
django-admin startproject myproject .
```

**Project Directory Structure:**
```text
myproject/
├── env/                   # Virtual environment folder
├── manage.py              # Django CLI utility
└── myproject/             # Project settings package
    ├── __init__.py
    ├── asgi.py
    ├── settings.py        # Central configuration file
    ├── urls.py            # Root URL routing
    └── wsgi.py
```

---

## 3. Creating a Django App

A Django project is a collection of apps. An app handles specific logic (e.g., users, products, blog, store).

Create a new app (e.g., `main` or `shop`):

```bash
python manage.py startapp shop
```

**Updated Structure:**
```text
myproject/
├── shop/                  # Newly created app
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py           # Views logic file
├── myproject/
│   └── ...
└── manage.py
```

---

## 4. Configuring Installed Apps

Tell your Django project that the new app exists by adding it to `settings.py`.

Open `myproject/settings.py` and add `'shop'` (or your app name) to `INSTALLED_APPS`:

```python
# myproject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom Apps
    'shop',
]
```

---

## 5. Creating Views

Views process user requests and return responses (either HTML pages or raw HTTP data).

Open `shop/views.py` and define your view functions:

```python
# shop/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Example 1: Basic HTTP Response View
def home(request):
    return HttpResponse("<h1>Welcome to SokoLink Home Page!</h1>")

# Example 2: HTML Template Render View
def about(request):
    context = {
        'title': 'About Us',
        'description': 'Welcome to our platform. We connect buyer and seller seamlessly.'
    }
    return render(request, 'shop/about.html', context)
```

---

## 6. Setting Up Templates

To render HTML files using `render()`, set up a template folder inside your app.

### Step 6.1: Create the Directory Structure
Create a `templates` folder inside `shop`, and a subfolder named `shop`:

```text
shop/
└── templates/
    └── shop/
        └── about.html
```

### Step 6.2: Create the Template File
Create `shop/templates/shop/about.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

---

## 7. Wiring Up URL Routing

URL routing connects web addresses (URLs) to your views.

### Step 7.1: Create App-Level URL File (`shop/urls.py`)
Create a new file named `urls.py` inside your app directory (`shop/urls.py`):

```python
# shop/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

### Step 7.2: Include App URLs in Main Project (`myproject/urls.py`)
Open the main URL file at `myproject/urls.py` and use `include` to connect the app's URLs:

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),  # Includes all URLs defined in shop/urls.py
]
```

---

## 8. Running the Development Server

### Step 8.1: Apply Default Database Migrations
Before starting the server for the first time, run default database migrations:

```bash
python manage.py migrate
```

### Step 8.2: Start the Server
Start Django's built-in web server:

```bash
python manage.py runserver
```

### Step 8.3: Verify in Browser
Open your browser and visit:
* **Home Page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **About Page:** [http://127.0.0.1:8000/about/](http://127.0.0.1:8000/about/)
* **Admin Interface:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 9. Troubleshooting & Quick Commands

| Issue / Action | Command / Solution |
| :--- | :--- |
| **`ImportError: Couldn't import Django`** | Make sure your virtual environment is activated (`env\Scripts\activate` or `source env/bin/activate`) before running `manage.py`. |
| **`ModuleNotFoundError`** | Ensure the package is installed inside the virtual environment (`pip install <package>`). |
| **Create a Superuser (Admin Access)** | `python manage.py createsuperuser` |
| **Save Installed Packages** | `pip freeze > requirements.txt` |
| **Install from `requirements.txt`** | `pip install -r requirements.txt` |
| **Deactivate Virtual Environment** | `deactivate` |