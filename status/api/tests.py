from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from status.models import Status
# Create your tests here.

User = get_user_model()


class StatusAPITestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='vojta', email='vojta@email.com')
        user.set_password('testpass')
        user.save()

        status_obj = Status.objects.create(user=user, summary='hello there')

    def test_statuses(self):
        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)

    def status_user_token(self):
        '''An extension for the following test.'''
        auth_url = api_reverse('api-auth:login')
        auth_data = {
            'username': 'vojta',
            'password': 'testpass',
        }
        auth_response = self.client.post(auth_url, auth_data, format='json')
        token = auth_response.data.get('token', 0)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

    def create_item(self):
        self.status_user_token() # Extension

        url = api_reverse('api-status:list')
        data = {
            'summary': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Status.objects.count(), 2)

        return response.data

    def test_status_create(self):
        data = self.create_item()
        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})
        rud_data = {
            'summary': 'another test content'
        }

        # get / retrieve
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_status_update(self):
        data = self.create_item()
        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})
        rud_data = {
            'summary': 'another test content'
        }
        put_response = self.client.put(rud_url, rud_data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        rud_response_data = put_response.data
        self.assertEqual(rud_response_data['summary'], rud_data['summary'])

    def test_status_delete(self):
        data = self.create_item()
        data_id = data.get('id')
        rud_url = api_reverse('api-status:detail', kwargs={'id': data_id})
        rud_data = {
            'summary': 'another test content'
        }
        del_response = self.client.delete(rud_url, format='json')
        self.assertEqual(del_response.status_code, status.HTTP_204_NO_CONTENT)

        # Another get/retrieve -> Not found
        get_response = self.client.get(rud_url, format='json')
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)

    def test_status_no_token_create(self):
        '''Same test, no extension -> no authentication.'''
        url = api_reverse('api-status:list')
        data = {
            'summary': 'some cool test content'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    # def test_register_user_api_fail(self):
    #     url = api_reverse('api-auth:register')
    #     data = {
    #         'username': 'vojta.test',
    #         'email:': 'vojta.test@email.com',
    #         'password': 'testpass',
    #     }
    #     response = self.client.post(url, data, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data['password2'][0], 'This field is required.')
    #
    # def test_register_user_api_success(self):
    #     url = api_reverse('api-auth:register')
    #     data = {
    #         'username': 'vojta.test',
    #         'email': 'vojtatest@email.com',
    #         'password': 'testpass',
    #         'password2': 'testpass'
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     token = response.data.get('token', 0)
    #     token_len = 0
    #     if token != 0:
    #         token_len = len(token)
    #     self.assertGreater(token_len, 0)
    #
    # def test_login_user_api(self):
    #     '''
    #     Use the credentials created in the setUp
    #     '''
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username': 'vojta',
    #         'password': 'testpass',
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     token = response.data.get('token', 0)
    #     token_len = 0
    #     if token != 0:
    #         token_len = len(token)
    #     self.assertGreater(token_len, 0)
    #
    # def test_login_user_api_fail(self):
    #     '''
    #     Use the credentials created in the setUp
    #     '''
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username': 'vojtafail',
    #         'password': 'testpass',
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #
    #     token = response.data.get('token', 0)
    #     token_len = 0
    #     if token != 0:
    #         token_len = len(token)
    #     self.assertEqual(token_len, 0)
    #
    # def test_token_login_api(self):
    #     '''
    #     Check that you can not login with a token that you have
    #     already logged in with.
    #     '''
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username': 'vojta',
    #         'password': 'testpass',
    #     }
    #     # First login successful
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     # Login while already logged in yields 403
    #     token = response.data.get('token', None)
    #     self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    #     response2 = self.client.post(url, data, format='json')
    #     self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)
    #
    # def test_token_register_api(self):
    #     url = api_reverse('api-auth:login')
    #     data = {
    #         'username': 'vojta',
    #         'password': 'testpass',
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     token = response.data.get('token', None)
    #     self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)
    #     url2 = api_reverse('api-auth:register')
    #     data2 = {
    #         'username': 'vojta.test',
    #         'email': 'vojtatest@email.com',
    #         'password': 'testpass',
    #         'password2': 'testpass'
    #     }
    #     response = self.client.post(url2, data2, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
