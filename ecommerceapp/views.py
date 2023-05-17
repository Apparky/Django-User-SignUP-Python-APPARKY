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
