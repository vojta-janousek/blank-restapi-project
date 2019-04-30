from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Status

# Create your tests here.

User = get_user_model()


class StatusTestCase(TestCase):

    def setUp(self):
        user = User.objects.create(username='vojta', email='vojta@email.com')
        user.set_password('testpass')
        user.save()

    def test_creating_status(self):
        user = User.objects.get(username='vojta')
        obj = Status.objects.create(user=user, summary='some cool content')
        self.assertEqual(obj.id, 1)

        qs = Status.objects.all()
        self.assertEqual(qs.count(), 1)
