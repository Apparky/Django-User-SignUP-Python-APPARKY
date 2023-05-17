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