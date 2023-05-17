from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handel_login, name='handel_login'),
    path('logout/', views.handel_logout, name='handel_logout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate')
]
