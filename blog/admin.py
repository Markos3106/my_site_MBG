from django.contrib import admin
from .models import *

"""
Configuració de l'administració del Blog.

Registra els models perquè siguin gestionables des del panell d'administració de Django.
"""

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)