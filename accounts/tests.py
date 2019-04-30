from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.

User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='vojta', email='vojta@email.com')
        user.set_password('testpass')
        user.save()

    def test_created_user(self):
        qs = User.objects.filter(username='vojta')
        self.assertEqual(qs.count(), 1)
