# Django-User-SignUP-Python-APPARKY

> In this Django Project we have designed a SignUP system of User for your Ecommerce site
> 
> We have agreed the terms and conditions of [Bootstrap](https://getbootstrap.com/) and have used free [Bootstrap](https://getbootstrap.com/) Templates in our work.
> 
> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Bootstrap is a free, open source front-end development framework for the creation of websites and web apps. 
> Designed to enable responsive development of mobile-first websites, Bootstrap provides a collection of syntax for template designs.
> 
> 

## Step 1:

Create a Folder first and open it from `CMD` (Windows) or your native `terminal`

Install [`Django`](https://www.djangoproject.com/) to your system by using this `command`

```commandline
pip install django
```

If done, create a new project file by typing this

```commandline
django-admin startproject YOURPROJECTNAME .
# In this project is the name of it is MyShop.
```

That's all. All your Native file will be created to yhe folder, and you are ready to start



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


## Step 3:

Previously we are done creating the `server`. Here we will add some `HTML` file with it

You can find it from [Bootstrap](https://getbootstrap.com/)

> Now create a folder named `static` and `templates`
> 
> Again go to `settings.py` file and follow this step
> 
> Find `TEMPLATES` section and alter this with the given billow lines

```commandline
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
``` 

> You will also find `STATIC` section, alter it accordingly with the given lines

```commandline
STATIC_URL = '/static/'

MIDEA_URL = '/midea/'
MIDEA_ROOT = os.path.join(BASE_DIR, 'midea')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

```

In your project Directory, all `html` file will be stored in it, and other `css`, `js` and other fill will be at `static` folder.

You can create or Download it from [Bootstrap](https://getbootstrap.com/) and arrange them accordingly

Here `index.html` is containing the `ContactUs` Form.

In the next step we will discuss how to set up all `.css`, `.js` and other file with `.html` file



## Step 4:

Previously we discuss setting up the `application` and the `HTML`, here w will discuss the `jinga` technique to set up `.css`, `.js` and other files with `.html`


Replace all `.css`, `.js` and other file location like this command billow

```commandline
"{% static 'js/jquery.min.js' %}"
```

```commandline
"{% static '/css/style.css' %}"
```

Before replacing that make sure in the `static` folder you have created the necessary sub folder 

In this case `css` and `js` are the sub folders

Now run the `server` and you'll see a `Contact Us` form will appair at [http://localhost:8000/](http://localhost:8000/), try the system, fill all the options and click `Send Message` 

Before runing the `server` you need to migrate the project so that the database and of it's cridientials are ready to strore the Feedback info.
To migrate copy the following command to your `terminal` 
```commndline
python manage.py makemigrations
```
```commandline
python manage.py migrate
```

We are all done. The `server` is ready to fire.

## Step 5:

For the Signup section let's create another Application named `authcart`

```commandline
python manage.py startapplication authcart
```
Now add `application` to the application list, and this is how it looks like.
```commandline
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "ecommerceapp",
    "authcart",
]
```

Now go back to application Directory, and edit your `urls.py` accordingly
```commandline
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handel_login, name='handel_login'),
    path('logout/', views.handel_logout, name='handel_logout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate')
]
```

And edit the `views.py` accordingly
```commandline
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View
from django_six import force_str
from .utils import TokenGenerator, generate_token
from django.core.mail import EmailMessage, send_mail
from django.conf import settings


def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')

        if password != confirm_password:
            messages.warning(request, "Password not Matched")
            return render(request, 'signup.html')

        try:
            if User.objects.get(username=email):
                messages.info(request, "Email has been taken")
                return render(request, 'signup.html')
#                    return HttpResponse("Email is already Exists")

        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password)
        user.is_active = False
        user.save()
        try:
            email_subject = "Activate Your Account"
            message = render_to_string('activate.html', {
                'user': user,
                'domain': '127.0.0.1:9000',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': generate_token.make_token(user)
            })

            email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
            email_message.send(fail_silently=False)
            messages.success(request, f"Activate your account by CLicking the link in your gmail {message}")
            return redirect('/auth/login/')

        except Exception as mail_error:
            messages.warning(request, "Email has been saved into our database")
            return redirect('/auth/login')


#            return HttpResponse("<h1>User Has been created Successfully</h1>")

    return render(request, 'signup.html')


def handel_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('pass1')

        try:
            if User.objects.get(username=email) is None:
                messages.warning(request, "User not Exists")
                return HttpResponse("USER not Exists")

            else:
                return render(request, 'index.html')

        except Exception as identification:
            pass

    return render(request, 'login.html')


def handel_logout(request):
    return redirect('/auth/login')

```



### Your project is ready... Run the `server` and enjoy 

### Happy learning

### To know more about [Django](https://www.djangoproject.com/) Click [Here](https://www.djangoproject.com/)


-------------------
> 
> To get more interesting follow you GitHub page at [Here](https://github.com/Apparky)
> 
> To know more about [APPARKY](https://apparky-soumenmtec-gmailcom.vercel.app/) Click [Here](https://apparky-soumenmtec-gmailcom.vercel.app/)
