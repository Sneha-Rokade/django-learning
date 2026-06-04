# Django Basics

## What is Django?

Django is a high-level Python web framework that allows developers to build secure, scalable, and maintainable web applications quickly.

It follows the MVT (Model-View-Template) architecture and comes with many built-in features such as:

* Authentication
* Admin Panel
* ORM (Object Relational Mapper)
* Session Management
* Security Features
* Form Handling

Official Website: https://www.djangoproject.com/

---

## Why Django?

### Advantages

* Fast Development
* Built-in Admin Interface
* Secure by Default
* Powerful ORM
* Large Community
* Scalable Architecture

### Use Cases

* Blogs
* E-commerce Websites
* Social Media Platforms
* Learning Management Systems
* Business Applications
* REST APIs

---

## Django Architecture (MVT)

### Model

Responsible for data and database operations.

Example:

class Post(models.Model):
    title = models.CharField(max_length=200)

### View

Handles application logic and user requests.

Example:

def home(request):
    return HttpResponse("Hello Django")

### Template

Responsible for displaying data to users.

Example: <h1>Welcome to Django</h1>

---

## Django Project vs App

### Project

The complete website/application.

Example: blog_project/

### App

A module that performs a specific task.

Examples:

blog/
users/
payments/
products/

A single project can contain multiple apps.

---

## Installation

Install Django:

pip install django

Verify installation:

django-admin --version

---

## Creating a Project

django-admin startproject blog_project

Project Structure:

blog_project/
│
├── manage.py
│
└── blog_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py

## Running Development Server

python manage.py runserver

Default URL:

http://127.0.0.1:8000

## Important Files

### manage.py

Command-line utility for Django operations.

Examples:
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser

### settings.py

Contains project configuration.

Examples:

* Installed Apps
* Database Settings
* Middleware
* Static Files
* Security Configuration

---

### urls.py

Maps URLs to views.

Example:
from django.urls import path

urlpatterns = [
]

## Creating an App

python manage.py startapp blog

Structure:

blog/
│
├── admin.py
├── apps.py
├── models.py
├── views.py
├── tests.py
└── migrations/

## Registering an App

Open settings.py:

INSTALLED_APPS = [
    'blog',
]

## Development Workflow

1. Create Project
2. Create App
3. Define URLs
4. Create Views
5. Create Templates
6. Create Models
7. Run Migrations
8. Test Application

---

## Key Interview Questions

### What is Django?

A high-level Python web framework that follows the MVT architecture.

### What is MVT?

Model-View-Template architecture used by Django.

### Difference Between Project and App?

Project = Entire application

App = Specific functionality within the application

### What is manage.py?

A command-line utility used for managing Django projects.

---

## Summary

In this chapter you learned:

* What Django is
* MVT Architecture
* Project vs App
* Installation
* Project Creation
* App Creation
* Development Workflow

