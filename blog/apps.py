from django.apps import AppConfig

"""
Configuració de l'aplicació Blog.

Defineix la configuració bàsica i el nom de l'app per a la seva integració al projecte Django.
"""


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
