from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, Http404
from operator import itemgetter
from .models import *


def index(request):
    try:
        latest_posts = Post.objects.order_by("-date")[:3]
        
        return render(request, 'blog/index.html', {"url_img": "/static/blog/img/gaming.jpg", "posts": latest_posts})
    
    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)

def posts(request):
    try:
        posts = Post.objects.all()
        return render(request, 'blog/posts.html', {"posts": posts})

    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)
        
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request, 'blog/post_detail.html', {"post": post})

    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)
    
def autors(request):
    try:
        autors = Author.objects.all()
        return render(request, 'blog/autors.html', {"autors": autors})

    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)
    
def autor_detail(request, first_name):
    try:
        autor = Author.objects.get(first_name=first_name)
        return render(request, 'blog/autor_detail.html', {"autor": autor, "posts": autor.posts.all()})

    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)
    
def tags(request):

    tags = Tag.objects.all()
    return render(request, 'blog/tags.html', {"tags": tags})


    
def tag_detail(request, caption):
    try:
        tag = Tag.objects.get(caption=caption)
        return render(request, 'blog/tag_detail.html', {"tag": tag, "posts": tag.posts.all()})

    except:
        response_data = render_to_string("blog/404.html")
        return HttpResponseNotFound(response_data)