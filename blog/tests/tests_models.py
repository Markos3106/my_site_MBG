from django.test import TestCase
from blog.models import Author, Post, Tag
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Marc", last_name="Rovira")
        self.tag1 = Tag.objects.create(name="RPG")
        self.tag2 = Tag.objects.create(name="Acció")

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
        self.assertEqual(str(self.author), "Marc Rovira")

    def test_post_author_relation(self):
        self.assertEqual(self.post.author, self.author)

    def test_post_tag_relation(self):
        self.assertIn(self.tag1, self.post.tags.all())
        self.assertIn(self.tag2, self.post.tags.all())

    def test_author_posts_reverse_relation(self):
        self.assertIn(self.post, self.author.posts.all())