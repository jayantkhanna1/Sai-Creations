"""saicreations_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name = "index"),
    path('index',views.index,name = "index"),
    path('add_to_newsletter',views.add_to_newsletter,name = "add_to_newsletter"),
    path('aboutus',views.about,name = "about"),
    path('contact',views.contact,name = "contact"),
    path('admin_login',views.admin_login,name = "admin_login"),
    path('admin_verified',views.admin_verified,name = "admin_verified"),
    path('login_admin',views.login_admin,name = "login_admin"),
    path('addproductpage',views.addproductpage,name= "addproductpage"),
    path('adminseeorders',views.adminseeorders,name= "adminseeorders"),
    path('add_product_to_database',views.add_product_to_database,name= "add_product_to_database"),
]
