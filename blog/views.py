from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseNotFound
from .models import *

"""
Vistes de l'aplicació Blog.

Aquest fitxer conté les funcions de vista que controlen la lògica de negoci
i gestionen les respostes HTTP per a cada ruta del blog.

Inclou la renderització de llistats de publicacions i detalls individuals.
"""

def index(request):
    """
    Vista principal del blog.

    Mostra les tres últimes publicacions a la pàgina inicial amb una imatge destacada.
    """
    try:
        latest_posts = Post.objects.order_by("-date")[:3]
        return render(request, 'blog/index.html', {"url_img": "/static/blog/img/gaming.jpg", "posts": latest_posts})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def posts(request):
    """
    Mostra totes les publicacions disponibles al blog.

    Aquesta vista carrega tots els objectes Post i els passa al template.
    """
    try:
        posts = Post.objects.all()
        return render(request, 'blog/posts.html', {"posts": posts})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def post_detail(request, slug):
    """
    Mostra el detall d'una publicació específica.

    Busca un post pel seu slug i mostra el seu contingut complet.
    """
    try:
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {"post": post})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def autors(request):
    """
    Mostra la llista de tots els autors del blog.
    """
    try:
        autors = Author.objects.all()
        return render(request, 'blog/autors.html', {"autors": autors})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def autor_detail(request, first_name):
    """
    Mostra el perfil d'un autor i les seves publicacions.

    Cerca un autor pel seu nom i mostra els seus detalls i posts relacionats.
    """
    try:
        autor = Author.objects.get(first_name=first_name)
        return render(request, 'blog/autor_detail.html', {"autor": autor, "posts": autor.posts.all()})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def tags(request):
    """
    Mostra tots els tags disponibles al blog.
    """
    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', {"tags": tags})

def tag_detail(request, caption):
    """
    Mostra les publicacions associades a un tag concret.

    Cerca el tag pel seu caption i carrega els seus posts relacionats.
    """
    try:
        tag = Tag.objects.get(caption=caption)
        return render(request, 'blog/tag_detail.html', {"tag": tag, "posts": tag.posts.all()})
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)
