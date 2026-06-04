# Django Templates

## What are Templates?

Templates are HTML files that allow us to display dynamic data from Django views.

Instead of returning plain text:

return HttpResponse("Hello Django")

we can render HTML:

return render(request, "home.html")

Templates separate presentation (UI) from business logic.

# Why Use Templates?

Without templates:
def home(request):
    return HttpResponse(
        "<h1>Welcome</h1>"
    )

This becomes difficult to maintain.

With templates:

def home(request):
    return render(
        request,
        "home.html"
    )

HTML stays inside dedicated files.

Benefits:

* Cleaner code
* Easier maintenance
* Better separation of concerns
* Reusable layouts

# Template Directory Structure

Recommended structure:
blog/
│
├── templates/
│   └── home.html

Project structure:
blog_project/
│
├── blog/
│   ├── templates/
│   │   └── home.html
│   ├── views.py
│   └── models.py

# Rendering a Template

### home.html

<h1>Welcome to Django</h1>

### views.py

from django.shortcuts import render

def home(request):
    return render(
        request,
        "home.html"
    )

# Passing Data to Templates

View:

def home(request):

    context = {
        "name": "Rahul"
    }

    return render(
        request,
        "home.html",
        context
    )

Template:
<h1>Hello {{ name }}</h1>

Output:
<h1>Hello Rahul</h1>

# Template Variables

Variables use double curly braces.

Syntax:

{{ variable }}

Example:

{{ title }}
{{ username }}
{{ email }}

# Multiple Variables

View:

def profile(request):

    context = {
        "name": "Rahul",
        "age": 25,
        "city": "Pune"
    }

    return render(
        request,
        "profile.html",
        context
    )

Template:

<h2>Name: {{ name }}</h2>
<h2>Age: {{ age }}</h2>
<h2>City: {{ city }}</h2>

# Template Tags

Template tags perform logic.

Syntax:

{% tag %}

Examples:

{% if %}
{% for %}
{% block %}
{% extends %}

# If Statement

Template:

{% if user.is_authenticated %}

<h1>Welcome User</h1>

{% endif %}

# If Else

{% if age >= 18 %}

Adult

{% else %}

Minor

{% endif %}

# For Loop

View:

context = {
    "students": [
        "Rahul",
        "Amit",
        "Priya"
    ]
}

Template:

{% for student in students %}

<p>{{ student }}</p>

{% endfor %}

Output:

Rahul
Amit
Priya

# Looping Through Models

View:

posts = Post.objects.all()

return render(
    request,
    "home.html",
    {"posts": posts}
)

Template:

{% for post in posts %}

<h2>{{ post.title }}</h2>

<p>{{ post.content }}</p>

{% endfor %}

# Empty Case

{% for post in posts %}

<h2>{{ post.title }}</h2>

{% empty %}

<p>No Posts Found</p>

{% endfor %}

# Template Filters

Filters modify values.

Syntax: {{ value|filter }}

## Uppercase

{{ name|upper }}

Output: RAHUL

## Lowercase

{{ name|lower }}

Output: rahul

## Length

{{ students|length }}

Output: 3

## Date Formatting

{{ created_at|date:"d-m-Y" }}

Output: 15-06-2026

# Template Inheritance

One of Django's most powerful features.

Instead of repeating HTML on every page.

# Base Template

base.html

<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
<nav>
    Home | About
</nav>
{% block content %}
{% endblock %}
</body>
</html>

# Child Template

home.html

{% extends 'base.html' %}

{% block content %}

<h1>Home Page</h1>

{% endblock %}

Output:

Navbar
Home Page

Benefits:

* Reusability
* Maintainability
* Consistent UI

# Including Templates

header.html

<nav>

Home

About

Contact

</nav>

home.html

{% include 'header.html' %}

# Static Files

Static files include:

* CSS
* JavaScript
* Images

Directory:

static/
│
├── css/
├── js/
└── images/

# Loading Static Files

Template:

{% load static %}

<link
rel="stylesheet"
href="{% static 'css/style.css' %}">

# Displaying Images

{% load static %}

<img src="{% static 'images/logo.png' %}">

# Common Template Errors

### TemplateDoesNotExist

Cause: Wrong template path

Solution: Verify templates folder structure

### Invalid Block Tag

Cause: Missing {% load %}

or typo in template tag.

# Best Practices

### Keep Logic in Views

Good: posts = Post.objects.all()

Bad: Complex calculations inside templates.

### Use Template Inheritance

Good:
base.html
home.html
about.html
contact.html

Avoid duplicating layouts.

### Use Meaningful Template Names

Good:
home.html
post_detail.html
student_list.html

Bad:
page1.html
test.html

# Interview Questions

### What is a Django Template?

An HTML file that can display dynamic data using Django Template Language (DTL).

### Difference Between {{ }} and {% %}

{{ }}

Used for variables.

{% %}

Used for logic and template tags.

### What is Template Inheritance?

A mechanism that allows child templates to reuse layouts from a parent template.

### What is a Context Dictionary?

Data passed from a view to a template.

Example:
{
    "name": "Rahul"
}

# Summary

In this chapter you learned:

* Templates
* Rendering HTML
* Variables
* Context
* Template Tags
* Loops
* Conditions
* Filters
* Template Inheritance
* Static Files

