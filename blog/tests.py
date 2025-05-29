from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Author, Post, Tag

"""
Tests generals de l'aplicació Blog.

Inclou proves automatitzades per comprovar el funcionament correcte dels components principals.
"""

class ViewTests(TestCase):
    """
    Proves de les vistes de l'aplicació Blog.

    Inclou tests per validar la resposta HTTP i el contingut retornat
    per les vistes de publicacions i autors.
    """

    def setUp(self):
        """
        Configura les dades de prova amb un autor i una publicació.
        """
        self.author = Author.objects.create(first_name="Roger", last_name="Font")
        self.post = Post.objects.create(
            title="Top FPS",
            content="Text del post",
            excerpt="Resum",
            slug="top-fps",
            date=timezone.now(),
            author=self.author
        )

    def test_post_list_view(self):
        """
        Comprova que la vista de llista de posts funcioni correctament.
        """
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Top FPS")

    def test_post_detail_view(self):
        """
        Comprova que la vista de detall d'un post funcioni correctament.
        """
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Text del post")

    def test_author_detail_view(self):
        """
        Comprova que la vista de detall d'autor retorni les dades correctes.
        """
        response = self.client.get(reverse('autor_detail', args=[self.author.first_name]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Roger")

class ModelTests(TestCase):
    """
    Proves de models del blog.

    Valida el comportament de les relacions i representació dels models.
    """

    def setUp(self):
        """
        Configura dades de prova per a models: autor, tags i post.
        """
        self.author = Author.objects.create(first_name="Marc", last_name="Rovira")
        self.tag1 = Tag.objects.create(caption="RPG")
        self.tag2 = Tag.objects.create(caption="Acció")

        self.post = Post.objects.create(
            title="Millors RPG 2025",
            content="Contingut del post...",
            excerpt="Resum...",
            slug="millors-rpg-2025",
            date=timezone.now(),
            author=self.author
        )
        self.post.tags.set([self.tag1, self.tag2])

    def test_author_str(self):
        """
        Comprova la representació en cadena del model Author.
        """
        self.assertEqual(str(self.author), "Marc Rovira")

    def test_post_author_relation(self):
        """
        Verifica que el post estigui relacionat correctament amb l'autor.
        """
        self.assertEqual(self.post.author, self.author)

    def test_post_tag_relation(self):
        """
        Comprova que els tags estiguin correctament associats al post.
        """
        self.assertIn(self.tag1, self.post.tags.all())
        self.assertIn(self.tag2, self.post.tags.all())

    def test_author_posts_reverse_relation(self):
        """
        Verifica que es pugui accedir als posts d’un autor mitjançant la relació inversa.
        """
        self.assertIn(self.post, self.author.posts.all())
