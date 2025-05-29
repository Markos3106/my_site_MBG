from django.urls import path
from . import views

"""
Rutes (URLs) de l'aplicació Blog.

Defineix els camins de l'aplicació i les vistes associades a cada URL.

Permet accedir a les diferents pàgines del blog com ara la pàgina principal i els detalls de publicació.
"""


urlpatterns = [
    path("", views.index, name="index"),
    path("post", views.posts, name="post"),
    path("post/<slug:slug>", views.post_detail, name="post_detail"),
    path("autor", views.autors, name="autor"),
    path("autor/<str:first_name>", views.autor_detail, name="autor_detail"),
    path("tag", views.tags, name="tag"),
    path("tag/<str:caption>", views.tag_detail, name="tag_detail")
]