from django.db import models

"""
Models de l'aplicació Blog.

Aquest fitxer defineix les classes de models que representen les dades del blog,
com ara publicacions, autors i etiquetes, i les seves relacions.

S'utilitza per gestionar la persistència de dades mitjançant l'ORM de Django.
"""

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    image = models.ImageField(upload_to='static/blog/img')
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title