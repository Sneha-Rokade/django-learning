# Django Models and ORM

## What is a Model?

A Model is a Python class that represents a database table.

Each attribute in the model becomes a column in the database table.

Example:

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

Database Table:

| id | title        | content         |
| -- | ------------ | --------------- |
| 1  | Django Intro | Learning Django |

---

## Why Use Models?

Models provide:

* Database abstraction
* Automatic SQL generation
* Data validation
* Relationships between tables
* Easier maintenance

Instead of writing SQL manually, Django generates SQL for you.

---

## What is ORM?

ORM stands for Object Relational Mapper.

ORM allows you to interact with databases using Python code instead of SQL.

Traditional SQL:

SELECT * FROM post;

Django ORM:

Post.objects.all()

---

## Creating Your First Model

Open:

blog/models.py

Create:

from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

## Common Field Types

### CharField

Stores short text.

name = models.CharField(max_length=100)

### TextField

Stores large text.

description = models.TextField()

### IntegerField

Stores integers.

age = models.IntegerField()

### FloatField

Stores decimal numbers.

price = models.FloatField()

### BooleanField

Stores True or False.

is_active = models.BooleanField(default=True)

### EmailField

Stores email addresses.

email = models.EmailField()

### DateTimeField

Stores date and time.

created_at = models.DateTimeField(
    auto_now_add=True
)

## Understanding Migrations

A migration is a file that tells Django how to create or modify database tables.

After creating a model:

python manage.py makemigrations

Example Output:

Migrations for 'blog':
  blog/migrations/0001_initial.py

Apply changes:

python manage.py migrate

## Registering Models in Admin Panel

Open:

blog/admin.py

Add:

from django.contrib import admin
from .models import Post

admin.site.register(Post)

Now Post can be managed through the admin dashboard.

## Creating Objects

Open Django Shell:

python manage.py shell

Import model:

from blog.models import Post

Create object:

Post.objects.create(
    title="First Post",
    content="Learning Django ORM"
)

## Reading Data

Get all records:

Post.objects.all()


Example:

posts = Post.objects.all()

for post in posts:
    print(post.title)

## Get Single Record

Using ID:

Post.objects.get(id=1)

Using title:

Post.objects.get(
    title="First Post"
)

## Filtering Records

Find specific records:

Post.objects.filter(
    title="Django"
)

Contains:

Post.objects.filter(
    title__contains="Django"
)

Starts With:

Post.objects.filter(
    title__startswith="Learn"
)

Ends With:

Post.objects.filter(
    title__endswith="Guide"
)

## Updating Records

Get object:

post = Post.objects.get(id=1)

Modify:

post.title = "Updated Title"

Save:

post.save()

## Deleting Records

Get object:

post = Post.objects.get(id=1)

Delete:

post.delete()

## Ordering Records

Ascending:

Post.objects.order_by(
    "title"
)

Descending:

Post.objects.order_by(
    "-created_at"
)

## Counting Records

Post.objects.count()

Example:

total_posts = Post.objects.count()

## Model Meta Class

Used for additional configuration.

Example:

class Post(models.Model):

    title = models.CharField(
        max_length=200
    )

    class Meta:
        ordering = ['-id']

This automatically sorts records by latest ID first.

## Best Practices

### Add **str**()

Good:

def __str__(self):
    return self.title

Bad:
# No __str__()

Without it, admin panel becomes difficult to read.

### Use Meaningful Names

Good:

title
content
created_at

Bad:

t
c
d

### Run Migrations Frequently

After every model change:

python manage.py makemigrations
python manage.py migrate

## Key Interview Questions

### What is a Django Model?

A Python class representing a database table.

### What is ORM?

Object Relational Mapper that allows database interaction using Python instead of SQL.

### Difference Between get() and filter()?

get()

Post.objects.get(id=1)

Returns one object.

Raises exception if not found.

filter()

Post.objects.filter(title="Django")

Returns a QuerySet.

Does not raise exception.

### What is Migration?

A mechanism that tracks and applies database schema changes.

### Why Use **str**()?

Provides a readable representation of model objects.

## Summary

In this chapter you learned:

* Models
* ORM
* Field Types
* Migrations
* CRUD Operations
* QuerySets
* Filtering
* Ordering
* Model Best Practices

