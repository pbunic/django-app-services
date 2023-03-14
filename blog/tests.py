from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title='My Post', slug='my-post', intro='introduction', body='content')

    def test_post_creation(self):
        post = Post.objects.get(id=1)
        post_expected = ['My Post', 'my-post', 'introduction', 'content']
        self.assertEqual(post.title, post_expected[0])
        self.assertEqual(post.slug, post_expected[1])
        self.assertEqual(post.intro, post_expected[2])
        self.assertEqual(post.body, post_expected[3])
