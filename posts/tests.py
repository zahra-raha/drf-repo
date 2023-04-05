from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='zahra', password='pass')

    def test_can_list_posts(self):
        zahra = User.objects.get(username='zahra')
        Post.objects.create(owner=zahra, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_loggedin_user_can_create_post(self):
        self.client.login(username="zahra", password="pass")
        response = self.client.post('/posts/', {'title': "a title"})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_loggedout_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'title': "a title"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# Create your tests here.