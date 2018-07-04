from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from blog.models import BlogPost, BlogCategory, BlogTag
from users.models import User


class CreateData:
    def create_data(self):
        self.category = BlogCategory.objects.create(title='Test Category')
        tag = BlogTag.objects.create(title='Test Tag')
        author = User.objects.create(name='hello', email='hello@gmail.com')
        self.blogpost = BlogPost.objects.create(title='title a', author=author, category=self.category, created_at=timezone.now())
        self.blogpost.tags.add(tag)


class BlogIndexTestCase(CreateData, TestCase):
    def setUp(self):
        self.create_data()
        self.url = reverse('blog:jobkurakani:index', args=[])
        super(BlogIndexTestCase, self).setUp()

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context_data(self):
        response = self.client.get(self.url)
        self.assertQuerysetEqual(response.context['object_list'], ['<BlogPost: title a>'])


class BlogPostByCategoryTestCase(CreateData, TestCase):
    def setUp(self):
        self.create_data()
        self.url = reverse('blog:jobkurakani:category_detail', args=[self.category.slug])
        super(BlogPostByCategoryTestCase, self).setUp()

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
