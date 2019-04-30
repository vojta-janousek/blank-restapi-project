from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Create your tests here.

User = get_user_model()


class UserAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='vojta', email='vojta@email.com')
        user.set_password('testpass')
        user.save()

    def test_created_user_std(self):
        qs = User.objects.filter(username='vojta')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'vojta.test',
            'email:': 'vojta.test@email.com',
            'password': 'testpass',
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api_success(self):
        url = api_reverse('api-auth:register')
        data = {
            'username': 'vojta.test',
            'email': 'vojtatest@email.com',
            'password': 'testpass',
            'password2': 'testpass'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        '''
        Use the credentials created in the setUp
        '''
        url = api_reverse('api-auth:login')
        data = {
            'username': 'vojta',
            'password': 'testpass',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        '''
        Use the credentials created in the setUp
        '''
        url = api_reverse('api-auth:login')
        data = {
            'username': 'vojtafail',
            'password': 'testpass',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        token = response.data.get('token', 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_token_login_api(self):
        '''
        Check that you can not login with a token that you have
        already logged in with.
        '''
        url = api_reverse('api-auth:login')
        data = {
            'username': 'vojta',
            'password': 'testpass',
        }
        # First login successful
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Login while already logged in yields 403
        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        url = api_reverse('api-auth:login')
        data = {
            'username': 'vojta',
            'password': 'testpass',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.data.get('token', None)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
        url2 = api_reverse('api-auth:register')
        data2 = {
            'username': 'vojta.test',
            'email': 'vojtatest@email.com',
            'password': 'testpass',
            'password2': 'testpass'
        }
        response = self.client.post(url2, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
