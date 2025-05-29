"""
Definició de rutes principals del projecte Django.

Inclou les URLs globals que apunten cap a les aplicacions internes com 'blog'.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"))
]
