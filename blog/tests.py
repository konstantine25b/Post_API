from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import Post, Comment

class PostAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a sample post
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_post(self):
        """Ensure we can create a new post object."""
        url = '/api/posts/'
        data = {'title': 'Another Test Post', 'content': 'Content of the post', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)

    def test_get_posts(self):
        """Ensure we can retrieve posts."""
        url = '/api/posts/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(post=self.post, content='Test Comment', author=self.user)

    def test_create_comment(self):
        """Ensure we can create a new comment object."""
        url = f'/api/comments/'
        data = {'post': self.post.id, 'content': 'Another Test Comment', 'author': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(Comment.objects.get(id=2).content, 'Another Test Comment')

    def test_get_comments(self):
        """Ensure we can retrieve comments."""
        url = '/api/comments/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)