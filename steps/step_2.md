## Step 2:

Now open the project file with the `IDLE` you like to use

Open the `terminal` from your `IDLE` and type 

```commandline
python manage.py runserver
```

> And you are good to go. Open this link form you browser [http://localhost:8001/](http://localhost:8001/)
> 
> You will see the `server` is running
> 
> 

Now Let's Create an application for our Ecommerce Page.

For Creating an Application type this to your `terminal`

```commandline
python manage.py startapplications ecommerceapp
```

You can see now a new folder has been created to your project directory

Now go to `settings.py` file you will find some list of installed application there

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
]
```

add the application name and save the file

```commandline
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'ecommerceapp', # app name has to insert here to make it work
]
```

like this


After that go to the application folder and create a new file named `urls.py`. Now you just have to register the application url to the project url

Go back to project directory, you will find another `urls.py`, edit the file accordingly

```commandline
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("contact/", views.contact, name='contact'),
    path("blog/", views.blog, name='blog'),
    path("about/", views.about, name='about'),
    path("orders/", views.orders, name='orders'),
    path("profile/", views.profile, name="my_profile"),

]

```

Now come back to Application directory and open `views.py` file

You can copy and paste the `code` from here

```commandline
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def contact(request):
    return render(request, "contact.html")


def about(request):
    return render(request, "about.html")


def orders(request):
    return render(request, "order.html")


def profile(request):
    return render(request, "my_profile.html")
# Create your views here.

```

Now the `server` is ready to go

By this your `database` is ready to store all your customers feedback

[Django](https://www.djangoproject.com/) use [sqlite3](https://sqlite.org/index.html) as a default `database`. To know more about [sqlite3](https://sqlite.org/index.html) Click [Here](https://sqlite.org/index.html)
