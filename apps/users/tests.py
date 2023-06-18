from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status

from apps.users.serializers import UserCreateSerializer

User = get_user_model()


class UserTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'display_name': 'Test User',
        }
    
    def test_create_user(self):
        response = self.client.post(
            '/users/',
            data=self.user_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        user = User.objects.get(username=self.user_data['username'])
        self.assertTrue(user.check_password(self.user_data['password']))


class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
            'display_name': 'Test User',
        }
        self.serializer = UserCreateSerializer(data=self.user_data)
    
    def test_serializer_with_valid_data(self):
        self.assertTrue(self.serializer.is_valid())
        user = self.serializer.save()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        self.assertTrue(user.check_password(self.user_data['password']))
        self.assertEqual(user.display_name, self.user_data['display_name'])
    
    def test_serializer_with_invalid_data(self):
        invalid_data = {'username': 'testuser'}
        serializer = UserCreateSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password', serializer.errors)
