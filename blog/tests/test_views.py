from django.test import TestCase
from django.urls import reverse
from blog.models import Author, Post
from django.utils import timezone

class ViewTests(TestCase):
    def setUp(self):
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
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Top FPS")

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Text del post")

    def test_author_detail_view(self):
        response = self.client.get(reverse('autor_detail', args=[self.author.first_name]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Roger")
