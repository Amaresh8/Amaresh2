"""Amaresh2 URL Configuration

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
from django.urls import path
from FB.views import *
from MG.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path("Django/",Django,name="Django"),
    path("Django2/",Django2,name="Django2"),
    path("Python/",Python,name="Python"),
    path("Python2/",Python2,name="Python2"),
    
]
